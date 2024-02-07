from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validate_and_create(self,http_request: HttpRequest ) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # business rule
        print("Inside tag_creator_view")
        print(http_request)
        print(product_code)
        # return http
        return HttpResponse(status_code=200,body={"Hello": "World"})
