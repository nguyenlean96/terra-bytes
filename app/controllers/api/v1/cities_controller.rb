class Api::V1::CitiesController < ApplicationController
  
  # GET /api/v1/cities
  def index
    # Check if request has limit parameter
    per_page = params[:limit].present? ? params[:limit].to_i : 10
    per_page = 50 if per_page > 50

    @cities = City.page(params[:page]).per(per_page)
      .order(name: :ASC, country_code: :ASC)
    render json: @cities
  end
end
