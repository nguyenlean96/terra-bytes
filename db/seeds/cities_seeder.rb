require "activerecord-import"
require "json"

# Get all the seeder files from the countries directory
seed_files = Dir[Rails.root.join("db", "seeds", "countries", "*_seeder.rb")]

# Loop through each file and seed the data
seed_files.each do |file|
  # Console out the file being seeded
  puts "Seeding #{file}"

  # Read the file and parse the JSON data
  city_data = eval(File.read(file))

  # Determine the batch size
  batch_size = 1000

  # Insert the data into the database using activerecord-import
  ActiveRecord::Base.transaction do
    city_data.each_slice(batch_size) do |batch|
      City.import batch, on_duplicate_key_ignore: true
    end
  end
end

puts "Cities seeded"