module ApiResponder
  extend ActiveSupport::Concern

  def success(data= nil, message: nil, code: 200)
    render json: {
      status: 'success',
      message: message,
      data: data
    }, status: code
  end

  def error(message: nil, code: 500)
    render json: {
      status: 'error',
      message: message
    }, status: code
  end