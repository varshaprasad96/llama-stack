# \ToolGroupsAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1ToolgroupsGet**](ToolGroupsAPI.md#V1ToolgroupsGet) | **Get** /v1/toolgroups | 
[**V1ToolgroupsPost**](ToolGroupsAPI.md#V1ToolgroupsPost) | **Post** /v1/toolgroups | 
[**V1ToolgroupsToolgroupIdDelete**](ToolGroupsAPI.md#V1ToolgroupsToolgroupIdDelete) | **Delete** /v1/toolgroups/{toolgroup_id} | 
[**V1ToolgroupsToolgroupIdGet**](ToolGroupsAPI.md#V1ToolgroupsToolgroupIdGet) | **Get** /v1/toolgroups/{toolgroup_id} | 
[**V1ToolsGet**](ToolGroupsAPI.md#V1ToolsGet) | **Get** /v1/tools | 
[**V1ToolsToolNameGet**](ToolGroupsAPI.md#V1ToolsToolNameGet) | **Get** /v1/tools/{tool_name} | 



## V1ToolgroupsGet

> ListToolGroupsResponse V1ToolgroupsGet(ctx).Execute()





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
	resp, r, err := apiClient.ToolGroupsAPI.V1ToolgroupsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolGroupsAPI.V1ToolgroupsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ToolgroupsGet`: ListToolGroupsResponse
	fmt.Fprintf(os.Stdout, "Response from `ToolGroupsAPI.V1ToolgroupsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolgroupsGetRequest struct via the builder pattern


### Return type

[**ListToolGroupsResponse**](ListToolGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ToolgroupsPost

> V1ToolgroupsPost(ctx).RegisterToolGroupRequest(registerToolGroupRequest).Execute()





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
	registerToolGroupRequest := *openapiclient.NewRegisterToolGroupRequest("ToolgroupId_example", "ProviderId_example") // RegisterToolGroupRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ToolGroupsAPI.V1ToolgroupsPost(context.Background()).RegisterToolGroupRequest(registerToolGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolGroupsAPI.V1ToolgroupsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolgroupsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registerToolGroupRequest** | [**RegisterToolGroupRequest**](RegisterToolGroupRequest.md) |  | 

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


## V1ToolgroupsToolgroupIdDelete

> V1ToolgroupsToolgroupIdDelete(ctx, toolgroupId).Execute()





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
	toolgroupId := "toolgroupId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ToolGroupsAPI.V1ToolgroupsToolgroupIdDelete(context.Background(), toolgroupId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolGroupsAPI.V1ToolgroupsToolgroupIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**toolgroupId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolgroupsToolgroupIdDeleteRequest struct via the builder pattern


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


## V1ToolgroupsToolgroupIdGet

> ToolGroup V1ToolgroupsToolgroupIdGet(ctx, toolgroupId).Execute()





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
	toolgroupId := "toolgroupId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ToolGroupsAPI.V1ToolgroupsToolgroupIdGet(context.Background(), toolgroupId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolGroupsAPI.V1ToolgroupsToolgroupIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ToolgroupsToolgroupIdGet`: ToolGroup
	fmt.Fprintf(os.Stdout, "Response from `ToolGroupsAPI.V1ToolgroupsToolgroupIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**toolgroupId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolgroupsToolgroupIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ToolGroup**](ToolGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ToolsGet

> ListToolsResponse V1ToolsGet(ctx).ToolgroupId(toolgroupId).Execute()





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
	toolgroupId := "toolgroupId_example" // string |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ToolGroupsAPI.V1ToolsGet(context.Background()).ToolgroupId(toolgroupId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolGroupsAPI.V1ToolsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ToolsGet`: ListToolsResponse
	fmt.Fprintf(os.Stdout, "Response from `ToolGroupsAPI.V1ToolsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toolgroupId** | **string** |  | 

### Return type

[**ListToolsResponse**](ListToolsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ToolsToolNameGet

> Tool V1ToolsToolNameGet(ctx, toolName).Execute()





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
	toolName := "toolName_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ToolGroupsAPI.V1ToolsToolNameGet(context.Background(), toolName).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolGroupsAPI.V1ToolsToolNameGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ToolsToolNameGet`: Tool
	fmt.Fprintf(os.Stdout, "Response from `ToolGroupsAPI.V1ToolsToolNameGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**toolName** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolsToolNameGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Tool**](Tool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

