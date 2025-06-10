from flask import Blueprint, jsonify, request, send_file, Response, current_app
import io
from typing import Union

from ..services.data_service import DataService

data_blueprint = Blueprint("data", __name__)

class DataController:
    def __init__(self, data_service: DataService):
        self.data_service = data_service

        data_blueprint.add_url_rule('/dados/submissoes', view_func=self.get_submissions)
        data_blueprint.add_url_rule('/dados/comentarios', view_func=self.get_comments)
        data_blueprint.add_url_rule('/exportar/submissoes/<formato>', view_func=self.export_submissions)
        data_blueprint.add_url_rule('/exportar/comentarios/<formato>', view_func=self.export_comments)
        data_blueprint.add_url_rule('/dados/contagem', view_func=self.get_counts)

    def get_submissions(self):
        try:
            page = int(request.args.get('page', 1))
            page_size = int(request.args.get('page_size', 10))

            # Obter o total de itens primeiro
            total_items = self.data_service.get_total_submissions()

            # Cálculo seguro de páginas
            total_pages = total_items // page_size
            if total_items % page_size > 0:
                total_pages += 1
            if total_pages == 0:
                total_pages = 1

            # Validar número da página
            if page < 1 or (total_items > 0 and page > total_pages):
                return jsonify({
                    "error": f"Página inválida. Páginas disponíveis: 1-{total_pages}",
                    "total": total_items
                }), 400

            result = self.data_service.get_submissions_paginated(page, page_size)

            # Se não houver dados mas a página é válida
            if not result.get("data"):
                return jsonify({
                    "data": [],
                    "total": total_items,
                    "current_page": page,
                    "total_pages": total_pages
                })

            return jsonify({
                "data": result["data"],
                "total": total_items,
                "current_page": page,
                "total_pages": total_pages
            })
        except Exception as e:
            current_app.logger.error(f"Erro em get_submissions: {str(e)}")
            return jsonify({"error": "Erro interno no servidor"}), 500

    def get_comments(self):
        try:
            page = int(request.args.get('page', 1))
            page_size = int(request.args.get('page_size', 10))

            # Obter o total de itens primeiro
            total_items = self.data_service.get_total_comments()

            # Cálculo seguro de páginas
            total_pages = total_items // page_size
            if total_items % page_size > 0:
                total_pages += 1
            if total_pages == 0:  # Garante pelo menos 1 página
                total_pages = 1

            # Validar número da página
            if page < 1 or (total_items > 0 and page > total_pages):
                return jsonify({
                    "error": f"Página inválida. Páginas disponíveis: 1-{total_pages}",
                    "total": total_items
                }), 400

            result = self.data_service.get_comments_paginated(page, page_size)

            # Se não houver dados mas a página é válida
            if not result.get("data"):
                return jsonify({
                    "data": [],
                    "total": total_items,
                    "current_page": page,
                    "total_pages": total_pages
                })

            return jsonify({
                "data": result["data"],
                "total": total_items,
                "current_page": page,
                "total_pages": total_pages
            })
        except Exception as e:
            current_app.logger.error(f"Erro em get_comments: {str(e)}")
            return jsonify({"error": "Erro interno no servidor"}), 500
    def get_counts(self):
        counts = self.data_service.get_counts()
        return jsonify(counts)

    def export_submissions(self, formato: str):
        return self._handle_export(
            export_func=self.data_service.export_submissions,
            formato=formato,
            filename_prefix="submissoes"
        )

    def export_comments(self, formato: str):
        return self._handle_export(
            export_func=self.data_service.export_comments,
            formato=formato,
            filename_prefix="comentarios"
        )

    def _handle_export(self, export_func, formato: str, filename_prefix: str) -> Union[Response, tuple]:
        try:
            # Verifica formato válido
            if formato not in ['csv', 'json']:
                return jsonify({"erro": "Formato inválido. Use 'csv' ou 'json'"}), 400

            # Executa a exportação
            resultado = export_func(format=formato)

            # Monta resposta
            if formato == 'csv':
                return send_file(
                    io.BytesIO(resultado.encode('utf-8')),
                    mimetype='text/csv',
                    as_attachment=True,
                    download_name=f'{filename_prefix}.csv'
                )
            else:
                return jsonify(resultado)

        except ValueError as e:
            return jsonify({"erro": str(e)}), 404
        except Exception as e:
            return jsonify({"erro": f"Erro interno: {str(e)}"}), 500
