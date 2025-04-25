# \ScoringFunctionsAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1ScoringFunctionsGet**](ScoringFunctionsAPI.md#V1ScoringFunctionsGet) | **Get** /v1/scoring-functions | 
[**V1ScoringFunctionsPost**](ScoringFunctionsAPI.md#V1ScoringFunctionsPost) | **Post** /v1/scoring-functions | 
[**V1ScoringFunctionsScoringFnIdGet**](ScoringFunctionsAPI.md#V1ScoringFunctionsScoringFnIdGet) | **Get** /v1/scoring-functions/{scoring_fn_id} | 



## V1ScoringFunctionsGet

> ListScoringFunctionsResponse V1ScoringFunctionsGet(ctx).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ScoringFunctionsAPI.V1ScoringFunctionsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ScoringFunctionsAPI.V1ScoringFunctionsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ScoringFunctionsGet`: ListScoringFunctionsResponse
	fmt.Fprintf(os.Stdout, "Response from `ScoringFunctionsAPI.V1ScoringFunctionsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1ScoringFunctionsGetRequest struct via the builder pattern


### Return type

[**ListScoringFunctionsResponse**](ListScoringFunctionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ScoringFunctionsPost

> V1ScoringFunctionsPost(ctx).RegisterScoringFunctionRequest(registerScoringFunctionRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	registerScoringFunctionRequest := *openapiclient.NewRegisterScoringFunctionRequest("ScoringFnId_example", "Description_example", openapiclient.ParamType{AgentTurnInputType: openapiclient.NewAgentTurnInputType("Type_example")}) // RegisterScoringFunctionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ScoringFunctionsAPI.V1ScoringFunctionsPost(context.Background()).RegisterScoringFunctionRequest(registerScoringFunctionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ScoringFunctionsAPI.V1ScoringFunctionsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ScoringFunctionsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registerScoringFunctionRequest** | [**RegisterScoringFunctionRequest**](RegisterScoringFunctionRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ScoringFunctionsScoringFnIdGet

> ScoringFn V1ScoringFunctionsScoringFnIdGet(ctx, scoringFnId).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	scoringFnId := "scoringFnId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ScoringFunctionsAPI.V1ScoringFunctionsScoringFnIdGet(context.Background(), scoringFnId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ScoringFunctionsAPI.V1ScoringFunctionsScoringFnIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ScoringFunctionsScoringFnIdGet`: ScoringFn
	fmt.Fprintf(os.Stdout, "Response from `ScoringFunctionsAPI.V1ScoringFunctionsScoringFnIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**scoringFnId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1ScoringFunctionsScoringFnIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ScoringFn**](ScoringFn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

