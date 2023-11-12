require "rails_helper"

RSpec.describe FileTranslationsController, type: :routing do
  describe "routing" do
    it "routes to #index" do
      expect(get: "/file_translations").to route_to("file_translations#index")
    end

    it "routes to #new" do
      expect(get: "/file_translations/new").to route_to("file_translations#new")
    end

    it "routes to #show" do
      expect(get: "/file_translations/1").to route_to("file_translations#show", id: "1")
    end

    it "routes to #edit" do
      expect(get: "/file_translations/1/edit").to route_to("file_translations#edit", id: "1")
    end


    it "routes to #create" do
      expect(post: "/file_translations").to route_to("file_translations#create")
    end

    it "routes to #update via PUT" do
      expect(put: "/file_translations/1").to route_to("file_translations#update", id: "1")
    end

    it "routes to #update via PATCH" do
      expect(patch: "/file_translations/1").to route_to("file_translations#update", id: "1")
    end

    it "routes to #destroy" do
      expect(delete: "/file_translations/1").to route_to("file_translations#destroy", id: "1")
    end
  end
end
