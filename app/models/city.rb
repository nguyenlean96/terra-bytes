class City < ApplicationRecord
  validates :name, presence: true
  validates :lat, presence: true, numericality: true
  validates :lon, presence: true, numericality: true
  validates :country_code, presence: true, length: { is: 2 }
  validates :state, presence: false # State is now optional

  # Ensure uniqueness based on the new unique index
  validates :name, uniqueness: { scope: [:country_code, :lat, :lon] }

  scope :by_country, ->(code) { where(country_code: code) }
  scope :by_name, ->(query) { where("name ILIKE ?", "%#{query}%") }
end
