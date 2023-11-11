class AddReviewedToExample < ActiveRecord::Migration[7.0]
  def change
    add_column :examples, :reviewed, :boolean, default: false
  end
end
