class Translation < ApplicationRecord

  scope :not_reviewed, -> { where(reviewed: false) }

  scope :reviewed, -> { where(reviewed: true) }
end
