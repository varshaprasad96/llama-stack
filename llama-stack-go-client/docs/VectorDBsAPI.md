# \VectorDBsAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1VectorDbsGet**](VectorDBsAPI.md#V1VectorDbsGet) | **Get** /v1/vector-dbs | 
[**V1VectorDbsPost**](VectorDBsAPI.md#V1VectorDbsPost) | **Post** /v1/vector-dbs | 
[**V1VectorDbsVectorDbIdDelete**](VectorDBsAPI.md#V1VectorDbsVectorDbIdDelete) | **Delete** /v1/vector-dbs/{vector_db_id} | 
[**V1VectorDbsVectorDbIdGet**](VectorDBsAPI.md#V1VectorDbsVectorDbIdGet) | **Get** /v1/vector-dbs/{vector_db_id} | 



## V1VectorDbsGet

> ListVectorDBsResponse V1VectorDbsGet(ctx).Execute()





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
	resp, r, err := apiClient.VectorDBsAPI.V1VectorDbsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VectorDBsAPI.V1VectorDbsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1VectorDbsGet`: ListVectorDBsResponse
	fmt.Fprintf(os.Stdout, "Response from `VectorDBsAPI.V1VectorDbsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1VectorDbsGetRequest struct via the builder pattern


### Return type

[**ListVectorDBsResponse**](ListVectorDBsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1VectorDbsPost

> VectorDB V1VectorDbsPost(ctx).RegisterVectorDbRequest(registerVectorDbRequest).Execute()





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
	registerVectorDbRequest := *openapiclient.NewRegisterVectorDbRequest("VectorDbId_example", "EmbeddingModel_example") // RegisterVectorDbRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VectorDBsAPI.V1VectorDbsPost(context.Background()).RegisterVectorDbRequest(registerVectorDbRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VectorDBsAPI.V1VectorDbsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1VectorDbsPost`: VectorDB
	fmt.Fprintf(os.Stdout, "Response from `VectorDBsAPI.V1VectorDbsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1VectorDbsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registerVectorDbRequest** | [**RegisterVectorDbRequest**](RegisterVectorDbRequest.md) |  | 

### Return type

[**VectorDB**](VectorDB.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1VectorDbsVectorDbIdDelete

> V1VectorDbsVectorDbIdDelete(ctx, vectorDbId).Execute()





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
	vectorDbId := "vectorDbId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.VectorDBsAPI.V1VectorDbsVectorDbIdDelete(context.Background(), vectorDbId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VectorDBsAPI.V1VectorDbsVectorDbIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**vectorDbId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1VectorDbsVectorDbIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1VectorDbsVectorDbIdGet

> VectorDB V1VectorDbsVectorDbIdGet(ctx, vectorDbId).Execute()





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
	vectorDbId := "vectorDbId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VectorDBsAPI.V1VectorDbsVectorDbIdGet(context.Background(), vectorDbId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VectorDBsAPI.V1VectorDbsVectorDbIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1VectorDbsVectorDbIdGet`: VectorDB
	fmt.Fprintf(os.Stdout, "Response from `VectorDBsAPI.V1VectorDbsVectorDbIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**vectorDbId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1VectorDbsVectorDbIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**VectorDB**](VectorDB.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

