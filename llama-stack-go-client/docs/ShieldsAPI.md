# \ShieldsAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1ShieldsGet**](ShieldsAPI.md#V1ShieldsGet) | **Get** /v1/shields | 
[**V1ShieldsIdentifierGet**](ShieldsAPI.md#V1ShieldsIdentifierGet) | **Get** /v1/shields/{identifier} | 
[**V1ShieldsPost**](ShieldsAPI.md#V1ShieldsPost) | **Post** /v1/shields | 



## V1ShieldsGet

> ListShieldsResponse V1ShieldsGet(ctx).Execute()





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
	resp, r, err := apiClient.ShieldsAPI.V1ShieldsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ShieldsAPI.V1ShieldsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ShieldsGet`: ListShieldsResponse
	fmt.Fprintf(os.Stdout, "Response from `ShieldsAPI.V1ShieldsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1ShieldsGetRequest struct via the builder pattern


### Return type

[**ListShieldsResponse**](ListShieldsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ShieldsIdentifierGet

> Shield V1ShieldsIdentifierGet(ctx, identifier).Execute()





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
	identifier := "identifier_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ShieldsAPI.V1ShieldsIdentifierGet(context.Background(), identifier).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ShieldsAPI.V1ShieldsIdentifierGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ShieldsIdentifierGet`: Shield
	fmt.Fprintf(os.Stdout, "Response from `ShieldsAPI.V1ShieldsIdentifierGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**identifier** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1ShieldsIdentifierGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Shield**](Shield.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ShieldsPost

> Shield V1ShieldsPost(ctx).RegisterShieldRequest(registerShieldRequest).Execute()





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
	registerShieldRequest := *openapiclient.NewRegisterShieldRequest("ShieldId_example") // RegisterShieldRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ShieldsAPI.V1ShieldsPost(context.Background()).RegisterShieldRequest(registerShieldRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ShieldsAPI.V1ShieldsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ShieldsPost`: Shield
	fmt.Fprintf(os.Stdout, "Response from `ShieldsAPI.V1ShieldsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ShieldsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registerShieldRequest** | [**RegisterShieldRequest**](RegisterShieldRequest.md) |  | 

### Return type

[**Shield**](Shield.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

