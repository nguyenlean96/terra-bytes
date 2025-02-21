class Api::V1::CitiesController < ApplicationController
  include ApiResponder
  
  # GET /api/v1/cities
  def index
    begin
      total_count = City.count
      # Check if request has limit parameter
      per_page = params[:limit].present? ? params[:limit].to_i : 10
      per_page = 50 if per_page > 50
      
      total_pages = (total_count / per_page).ceil
      
      @cities = City.page(params[:page]).per(per_page)
        .order(name: :ASC, country_code: :ASC)
      success data: {
        data: @cities,
        meta: {
          current_page: params[:page].present? ? params[:page].to_i : 1,
          total_count: total_count,
          total_pages: total_pages,
        }
      }
    rescue => e
      error(message: e.message)
    end
  end
end
