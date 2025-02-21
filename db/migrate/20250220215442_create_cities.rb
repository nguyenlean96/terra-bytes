class CreateCities < ActiveRecord::Migration[8.0]
  def up
    create_table :cities do |t|
      t.string :name, null: false
      t.string :state, null: true
      t.string :country
      t.string :country_code, limit: 2, null: false
      t.integer :timezone_offset
      t.integer :population
      t.decimal :lat, precision: 12, scale: 8, null: false
      t.decimal :lon, precision: 12, scale: 8, null: false

      t.timestamps
    end

    # Add a unique index to prevent duplicates
    add_index :cities, [:name, :country_code, :lat, :lon], unique: true
  end

  def down
    drop_table :cities, if_exists: true
  end
end
