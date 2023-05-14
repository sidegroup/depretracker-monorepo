class Example < ApplicationRecord

  scope :not_reviewed, -> { where(reviewed: false) }
end
