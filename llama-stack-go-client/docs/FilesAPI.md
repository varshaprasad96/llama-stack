# \FilesAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1FilesBucketGet**](FilesAPI.md#V1FilesBucketGet) | **Get** /v1/files/{bucket} | 
[**V1FilesBucketKeyDelete**](FilesAPI.md#V1FilesBucketKeyDelete) | **Delete** /v1/files/{bucket}/{key} | 
[**V1FilesBucketKeyGet**](FilesAPI.md#V1FilesBucketKeyGet) | **Get** /v1/files/{bucket}/{key} | 
[**V1FilesGet**](FilesAPI.md#V1FilesGet) | **Get** /v1/files | 
[**V1FilesPost**](FilesAPI.md#V1FilesPost) | **Post** /v1/files | 
[**V1FilesSessionUploadIdGet**](FilesAPI.md#V1FilesSessionUploadIdGet) | **Get** /v1/files/session:{upload_id} | 
[**V1FilesSessionUploadIdPost**](FilesAPI.md#V1FilesSessionUploadIdPost) | **Post** /v1/files/session:{upload_id} | 



## V1FilesBucketGet

> ListFileResponse V1FilesBucketGet(ctx, bucket).Execute()





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
	bucket := "bucket_example" // string | Bucket name (valid chars: a-zA-Z0-9_-)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FilesAPI.V1FilesBucketGet(context.Background(), bucket).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.V1FilesBucketGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1FilesBucketGet`: ListFileResponse
	fmt.Fprintf(os.Stdout, "Response from `FilesAPI.V1FilesBucketGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**bucket** | **string** | Bucket name (valid chars: a-zA-Z0-9_-) | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1FilesBucketGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ListFileResponse**](ListFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1FilesBucketKeyDelete

> V1FilesBucketKeyDelete(ctx, bucket, key).Execute()





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
	bucket := "bucket_example" // string | Bucket name (valid chars: a-zA-Z0-9_-)
	key := "key_example" // string | Key under which the file is stored (valid chars: a-zA-Z0-9_-/.)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.FilesAPI.V1FilesBucketKeyDelete(context.Background(), bucket, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.V1FilesBucketKeyDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**bucket** | **string** | Bucket name (valid chars: a-zA-Z0-9_-) | 
**key** | **string** | Key under which the file is stored (valid chars: a-zA-Z0-9_-/.) | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1FilesBucketKeyDeleteRequest struct via the builder pattern


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


## V1FilesBucketKeyGet

> FileResponse V1FilesBucketKeyGet(ctx, bucket, key).Execute()





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
	bucket := "bucket_example" // string | Bucket name (valid chars: a-zA-Z0-9_-)
	key := "key_example" // string | Key under which the file is stored (valid chars: a-zA-Z0-9_-/.)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FilesAPI.V1FilesBucketKeyGet(context.Background(), bucket, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.V1FilesBucketKeyGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1FilesBucketKeyGet`: FileResponse
	fmt.Fprintf(os.Stdout, "Response from `FilesAPI.V1FilesBucketKeyGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**bucket** | **string** | Bucket name (valid chars: a-zA-Z0-9_-) | 
**key** | **string** | Key under which the file is stored (valid chars: a-zA-Z0-9_-/.) | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1FilesBucketKeyGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**FileResponse**](FileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1FilesGet

> ListBucketResponse V1FilesGet(ctx).Bucket(bucket).Execute()





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
	bucket := "bucket_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FilesAPI.V1FilesGet(context.Background()).Bucket(bucket).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.V1FilesGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1FilesGet`: ListBucketResponse
	fmt.Fprintf(os.Stdout, "Response from `FilesAPI.V1FilesGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1FilesGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **string** |  | 

### Return type

[**ListBucketResponse**](ListBucketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1FilesPost

> FileUploadResponse V1FilesPost(ctx).CreateUploadSessionRequest(createUploadSessionRequest).Execute()





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
	createUploadSessionRequest := *openapiclient.NewCreateUploadSessionRequest("Bucket_example", "Key_example", "MimeType_example", int32(123)) // CreateUploadSessionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FilesAPI.V1FilesPost(context.Background()).CreateUploadSessionRequest(createUploadSessionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.V1FilesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1FilesPost`: FileUploadResponse
	fmt.Fprintf(os.Stdout, "Response from `FilesAPI.V1FilesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1FilesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createUploadSessionRequest** | [**CreateUploadSessionRequest**](CreateUploadSessionRequest.md) |  | 

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1FilesSessionUploadIdGet

> FileUploadResponse V1FilesSessionUploadIdGet(ctx, uploadId).Execute()





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
	uploadId := "uploadId_example" // string | ID of the upload session

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FilesAPI.V1FilesSessionUploadIdGet(context.Background(), uploadId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.V1FilesSessionUploadIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1FilesSessionUploadIdGet`: FileUploadResponse
	fmt.Fprintf(os.Stdout, "Response from `FilesAPI.V1FilesSessionUploadIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**uploadId** | **string** | ID of the upload session | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1FilesSessionUploadIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1FilesSessionUploadIdPost

> FileResponse V1FilesSessionUploadIdPost(ctx, uploadId).Body(body).Execute()





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
	uploadId := "uploadId_example" // string | ID of the upload session
	body := os.NewFile(1234, "some_file") // *os.File | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.FilesAPI.V1FilesSessionUploadIdPost(context.Background(), uploadId).Body(body).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `FilesAPI.V1FilesSessionUploadIdPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1FilesSessionUploadIdPost`: FileResponse
	fmt.Fprintf(os.Stdout, "Response from `FilesAPI.V1FilesSessionUploadIdPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**uploadId** | **string** | ID of the upload session | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1FilesSessionUploadIdPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **body** | ***os.File** |  | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

