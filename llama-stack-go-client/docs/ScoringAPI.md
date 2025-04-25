# \ScoringAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1ScoringScoreBatchPost**](ScoringAPI.md#V1ScoringScoreBatchPost) | **Post** /v1/scoring/score-batch | 
[**V1ScoringScorePost**](ScoringAPI.md#V1ScoringScorePost) | **Post** /v1/scoring/score | 



## V1ScoringScoreBatchPost

> ScoreBatchResponse V1ScoringScoreBatchPost(ctx).ScoreBatchRequest(scoreBatchRequest).Execute()





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
	scoreBatchRequest := *openapiclient.NewScoreBatchRequest("DatasetId_example", map[string]ScoreRequestScoringFunctionsValue{"key": openapiclient.ScoreRequest_scoring_functions_value{ScoringFnParams: openapiclient.ScoringFnParams{BasicScoringFnParams: openapiclient.NewBasicScoringFnParams("Type_example")}}}, false) // ScoreBatchRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ScoringAPI.V1ScoringScoreBatchPost(context.Background()).ScoreBatchRequest(scoreBatchRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ScoringAPI.V1ScoringScoreBatchPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ScoringScoreBatchPost`: ScoreBatchResponse
	fmt.Fprintf(os.Stdout, "Response from `ScoringAPI.V1ScoringScoreBatchPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ScoringScoreBatchPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoreBatchRequest** | [**ScoreBatchRequest**](ScoreBatchRequest.md) |  | 

### Return type

[**ScoreBatchResponse**](ScoreBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ScoringScorePost

> ScoreResponse V1ScoringScorePost(ctx).ScoreRequest(scoreRequest).Execute()





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
	scoreRequest := *openapiclient.NewScoreRequest([]map[string]AppendRowsRequestRowsInnerValue{map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}}, map[string]ScoreRequestScoringFunctionsValue{"key": openapiclient.ScoreRequest_scoring_functions_value{ScoringFnParams: openapiclient.ScoringFnParams{BasicScoringFnParams: openapiclient.NewBasicScoringFnParams("Type_example")}}}) // ScoreRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ScoringAPI.V1ScoringScorePost(context.Background()).ScoreRequest(scoreRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ScoringAPI.V1ScoringScorePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ScoringScorePost`: ScoreResponse
	fmt.Fprintf(os.Stdout, "Response from `ScoringAPI.V1ScoringScorePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ScoringScorePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scoreRequest** | [**ScoreRequest**](ScoreRequest.md) |  | 

### Return type

[**ScoreResponse**](ScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

