require 'rails_helper'

RSpec.describe UserFilesHelper, type: :helper do
  let(:expected_header) { ['COLUMN 1','COLUMN 2','COLUMN 3'] }
  let(:expected_rows) { [%w[A 1 AAA\ AAA\ AAA], %w[B 2 BBB\ BBB\ BBB]] }

  context 'CSV file' do
    let(:user_file) { create(:user_file) }

    describe '#file_type' do
      it { expect(helper.file_type(user_file)).to eq('text/csv') }
    end

    describe '#file_header' do
      it { expect(helper.file_header(user_file)).to eq(expected_header) }
    end

    describe '#file_rows' do
      it { expect(helper.file_rows(user_file)).to eq(expected_rows) }
    end
  end

  context 'TSV file' do
    let(:user_file) { create(:user_file, :with_tsv) }

    describe '#file_type' do
      it { expect(helper.file_type(user_file)).to eq('text/tab-separated-values') }
    end

    describe '#file_header' do
      it { expect(helper.file_header(user_file)).to eq(expected_header) }
    end

    describe '#file_rows' do
      it { expect(helper.file_rows(user_file)).to eq(expected_rows) }
    end
  end
end