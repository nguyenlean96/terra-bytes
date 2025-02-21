class Api::V1::CitiesController < ApplicationController
  
  # GET /api/v1/cities
  def index
    @cities = City.order(name: :ASC, country_code: :ASC)
    render json: @cities
  end
end
