# \ModelsAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1ModelsGet**](ModelsAPI.md#V1ModelsGet) | **Get** /v1/models | 
[**V1ModelsModelIdDelete**](ModelsAPI.md#V1ModelsModelIdDelete) | **Delete** /v1/models/{model_id} | 
[**V1ModelsModelIdGet**](ModelsAPI.md#V1ModelsModelIdGet) | **Get** /v1/models/{model_id} | 
[**V1ModelsPost**](ModelsAPI.md#V1ModelsPost) | **Post** /v1/models | 
[**V1OpenaiV1ModelsGet**](ModelsAPI.md#V1OpenaiV1ModelsGet) | **Get** /v1/openai/v1/models | 



## V1ModelsGet

> ListModelsResponse V1ModelsGet(ctx).Execute()





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
	resp, r, err := apiClient.ModelsAPI.V1ModelsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ModelsAPI.V1ModelsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ModelsGet`: ListModelsResponse
	fmt.Fprintf(os.Stdout, "Response from `ModelsAPI.V1ModelsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1ModelsGetRequest struct via the builder pattern


### Return type

[**ListModelsResponse**](ListModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ModelsModelIdDelete

> V1ModelsModelIdDelete(ctx, modelId).Execute()





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
	modelId := "modelId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ModelsAPI.V1ModelsModelIdDelete(context.Background(), modelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ModelsAPI.V1ModelsModelIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**modelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1ModelsModelIdDeleteRequest struct via the builder pattern


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


## V1ModelsModelIdGet

> Model V1ModelsModelIdGet(ctx, modelId).Execute()





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
	modelId := "modelId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ModelsAPI.V1ModelsModelIdGet(context.Background(), modelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ModelsAPI.V1ModelsModelIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ModelsModelIdGet`: Model
	fmt.Fprintf(os.Stdout, "Response from `ModelsAPI.V1ModelsModelIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**modelId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1ModelsModelIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ModelsPost

> Model V1ModelsPost(ctx).RegisterModelRequest(registerModelRequest).Execute()





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
	registerModelRequest := *openapiclient.NewRegisterModelRequest("ModelId_example") // RegisterModelRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ModelsAPI.V1ModelsPost(context.Background()).RegisterModelRequest(registerModelRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ModelsAPI.V1ModelsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ModelsPost`: Model
	fmt.Fprintf(os.Stdout, "Response from `ModelsAPI.V1ModelsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ModelsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registerModelRequest** | [**RegisterModelRequest**](RegisterModelRequest.md) |  | 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1OpenaiV1ModelsGet

> OpenAIListModelsResponse V1OpenaiV1ModelsGet(ctx).Execute()





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
	resp, r, err := apiClient.ModelsAPI.V1OpenaiV1ModelsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ModelsAPI.V1OpenaiV1ModelsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1OpenaiV1ModelsGet`: OpenAIListModelsResponse
	fmt.Fprintf(os.Stdout, "Response from `ModelsAPI.V1OpenaiV1ModelsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1OpenaiV1ModelsGetRequest struct via the builder pattern


### Return type

[**OpenAIListModelsResponse**](OpenAIListModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

