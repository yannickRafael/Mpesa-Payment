from pprint import pprint
from config import api_context as api_context
from portalsdk import APIContext, APIMethodType, APIRequest


def pay(TransactionReference, CustomerMSISDN, Amount, ThirdPartyReference, ServiceProviderCode):

    api_con = api_context

    api_context.add_header('Origin', '*')

    api_con.add_parameter('input_TransactionReference', TransactionReference)
    api_con.add_parameter('input_CustomerMSISDN', CustomerMSISDN)
    api_con.add_parameter('input_Amount', Amount)
    api_con.add_parameter('input_ThirdPartyReference', ThirdPartyReference)
    api_con.add_parameter('input_ServiceProviderCode', ServiceProviderCode)

    api_request = APIRequest(api_con)
    result = api_request.execute()

    pprint(result.status_code)
    pprint(result.headers)
    pprint(result.body)


if __name__ == '__main__':
    # TransactionReference = 'T12344C'
    # CustomerMSISDN = '258844236139'
    # Amount = '10'
    # ThirdPartyReference = '111PA2D3'
    # ServiceProviderCode = '171717'

    #pay(TransactionReference, CustomerMSISDN, Amount, ThirdPartyReference, ServiceProviderCode)

