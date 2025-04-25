# \AgentsAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1AgentsAgentIdDelete**](AgentsAPI.md#V1AgentsAgentIdDelete) | **Delete** /v1/agents/{agent_id} | 
[**V1AgentsAgentIdGet**](AgentsAPI.md#V1AgentsAgentIdGet) | **Get** /v1/agents/{agent_id} | 
[**V1AgentsAgentIdSessionPost**](AgentsAPI.md#V1AgentsAgentIdSessionPost) | **Post** /v1/agents/{agent_id}/session | 
[**V1AgentsAgentIdSessionSessionIdDelete**](AgentsAPI.md#V1AgentsAgentIdSessionSessionIdDelete) | **Delete** /v1/agents/{agent_id}/session/{session_id} | 
[**V1AgentsAgentIdSessionSessionIdGet**](AgentsAPI.md#V1AgentsAgentIdSessionSessionIdGet) | **Get** /v1/agents/{agent_id}/session/{session_id} | 
[**V1AgentsAgentIdSessionSessionIdTurnPost**](AgentsAPI.md#V1AgentsAgentIdSessionSessionIdTurnPost) | **Post** /v1/agents/{agent_id}/session/{session_id}/turn | 
[**V1AgentsAgentIdSessionSessionIdTurnTurnIdGet**](AgentsAPI.md#V1AgentsAgentIdSessionSessionIdTurnTurnIdGet) | **Get** /v1/agents/{agent_id}/session/{session_id}/turn/{turn_id} | 
[**V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost**](AgentsAPI.md#V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost) | **Post** /v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/resume | 
[**V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet**](AgentsAPI.md#V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet) | **Get** /v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}/step/{step_id} | 
[**V1AgentsAgentIdSessionsGet**](AgentsAPI.md#V1AgentsAgentIdSessionsGet) | **Get** /v1/agents/{agent_id}/sessions | 
[**V1AgentsGet**](AgentsAPI.md#V1AgentsGet) | **Get** /v1/agents | 
[**V1AgentsPost**](AgentsAPI.md#V1AgentsPost) | **Post** /v1/agents | 



## V1AgentsAgentIdDelete

> V1AgentsAgentIdDelete(ctx, agentId).Execute()





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
	agentId := "agentId_example" // string | The ID of the agent to delete.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AgentsAPI.V1AgentsAgentIdDelete(context.Background(), agentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | The ID of the agent to delete. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdDeleteRequest struct via the builder pattern


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


## V1AgentsAgentIdGet

> Agent V1AgentsAgentIdGet(ctx, agentId).Execute()





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
	agentId := "agentId_example" // string | ID of the agent.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdGet(context.Background(), agentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdGet`: Agent
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | ID of the agent. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Agent**](Agent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsAgentIdSessionPost

> AgentSessionCreateResponse V1AgentsAgentIdSessionPost(ctx, agentId).CreateAgentSessionRequest(createAgentSessionRequest).Execute()





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
	agentId := "agentId_example" // string | The ID of the agent to create the session for.
	createAgentSessionRequest := *openapiclient.NewCreateAgentSessionRequest("SessionName_example") // CreateAgentSessionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionPost(context.Background(), agentId).CreateAgentSessionRequest(createAgentSessionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdSessionPost`: AgentSessionCreateResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdSessionPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | The ID of the agent to create the session for. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **createAgentSessionRequest** | [**CreateAgentSessionRequest**](CreateAgentSessionRequest.md) |  | 

### Return type

[**AgentSessionCreateResponse**](AgentSessionCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsAgentIdSessionSessionIdDelete

> V1AgentsAgentIdSessionSessionIdDelete(ctx, sessionId, agentId).Execute()





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
	sessionId := "sessionId_example" // string | The ID of the session to delete.
	agentId := "agentId_example" // string | The ID of the agent to delete the session for.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionSessionIdDelete(context.Background(), sessionId, agentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionSessionIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**sessionId** | **string** | The ID of the session to delete. | 
**agentId** | **string** | The ID of the agent to delete the session for. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionSessionIdDeleteRequest struct via the builder pattern


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


## V1AgentsAgentIdSessionSessionIdGet

> Session V1AgentsAgentIdSessionSessionIdGet(ctx, sessionId, agentId).TurnIds(turnIds).Execute()





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
	sessionId := "sessionId_example" // string | The ID of the session to get.
	agentId := "agentId_example" // string | The ID of the agent to get the session for.
	turnIds := []string{"Inner_example"} // []string | (Optional) List of turn IDs to filter the session by. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionSessionIdGet(context.Background(), sessionId, agentId).TurnIds(turnIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionSessionIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdSessionSessionIdGet`: Session
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdSessionSessionIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**sessionId** | **string** | The ID of the session to get. | 
**agentId** | **string** | The ID of the agent to get the session for. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionSessionIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **turnIds** | **[]string** | (Optional) List of turn IDs to filter the session by. | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsAgentIdSessionSessionIdTurnPost

> Turn V1AgentsAgentIdSessionSessionIdTurnPost(ctx, agentId, sessionId).CreateAgentTurnRequest(createAgentTurnRequest).Execute()





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
	agentId := "agentId_example" // string | The ID of the agent to create the turn for.
	sessionId := "sessionId_example" // string | The ID of the session to create the turn for.
	createAgentTurnRequest := *openapiclient.NewCreateAgentTurnRequest([]openapiclient.CreateAgentTurnRequestMessagesInner{openapiclient.CreateAgentTurnRequest_messages_inner{ToolResponseMessage: openapiclient.NewToolResponseMessage("Role_example", "CallId_example", openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}})}}) // CreateAgentTurnRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnPost(context.Background(), agentId, sessionId).CreateAgentTurnRequest(createAgentTurnRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdSessionSessionIdTurnPost`: Turn
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | The ID of the agent to create the turn for. | 
**sessionId** | **string** | The ID of the session to create the turn for. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionSessionIdTurnPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **createAgentTurnRequest** | [**CreateAgentTurnRequest**](CreateAgentTurnRequest.md) |  | 

### Return type

[**Turn**](Turn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsAgentIdSessionSessionIdTurnTurnIdGet

> Turn V1AgentsAgentIdSessionSessionIdTurnTurnIdGet(ctx, agentId, sessionId, turnId).Execute()





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
	agentId := "agentId_example" // string | The ID of the agent to get the turn for.
	sessionId := "sessionId_example" // string | The ID of the session to get the turn for.
	turnId := "turnId_example" // string | The ID of the turn to get.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdGet(context.Background(), agentId, sessionId, turnId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdSessionSessionIdTurnTurnIdGet`: Turn
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | The ID of the agent to get the turn for. | 
**sessionId** | **string** | The ID of the session to get the turn for. | 
**turnId** | **string** | The ID of the turn to get. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionSessionIdTurnTurnIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




### Return type

[**Turn**](Turn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost

> Turn V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost(ctx, agentId, sessionId, turnId).ResumeAgentTurnRequest(resumeAgentTurnRequest).Execute()





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
	agentId := "agentId_example" // string | The ID of the agent to resume.
	sessionId := "sessionId_example" // string | The ID of the session to resume.
	turnId := "turnId_example" // string | The ID of the turn to resume.
	resumeAgentTurnRequest := *openapiclient.NewResumeAgentTurnRequest([]openapiclient.ToolResponse{*openapiclient.NewToolResponse("CallId_example", openapiclient.ToolCall_tool_name{String: new(string)}, openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}})}) // ResumeAgentTurnRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost(context.Background(), agentId, sessionId, turnId).ResumeAgentTurnRequest(resumeAgentTurnRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost`: Turn
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdResumePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | The ID of the agent to resume. | 
**sessionId** | **string** | The ID of the session to resume. | 
**turnId** | **string** | The ID of the turn to resume. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionSessionIdTurnTurnIdResumePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



 **resumeAgentTurnRequest** | [**ResumeAgentTurnRequest**](ResumeAgentTurnRequest.md) |  | 

### Return type

[**Turn**](Turn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet

> AgentStepResponse V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet(ctx, agentId, sessionId, turnId, stepId).Execute()





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
	agentId := "agentId_example" // string | The ID of the agent to get the step for.
	sessionId := "sessionId_example" // string | The ID of the session to get the step for.
	turnId := "turnId_example" // string | The ID of the turn to get the step for.
	stepId := "stepId_example" // string | The ID of the step to get.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet(context.Background(), agentId, sessionId, turnId, stepId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet`: AgentStepResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | The ID of the agent to get the step for. | 
**sessionId** | **string** | The ID of the session to get the step for. | 
**turnId** | **string** | The ID of the turn to get the step for. | 
**stepId** | **string** | The ID of the step to get. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionSessionIdTurnTurnIdStepStepIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------





### Return type

[**AgentStepResponse**](AgentStepResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsAgentIdSessionsGet

> ListAgentSessionsResponse V1AgentsAgentIdSessionsGet(ctx, agentId).Execute()





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
	agentId := "agentId_example" // string | The ID of the agent to list sessions for.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsAgentIdSessionsGet(context.Background(), agentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsAgentIdSessionsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsAgentIdSessionsGet`: ListAgentSessionsResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsAgentIdSessionsGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**agentId** | **string** | The ID of the agent to list sessions for. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsAgentIdSessionsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ListAgentSessionsResponse**](ListAgentSessionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsGet

> ListAgentsResponse V1AgentsGet(ctx).Execute()





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
	resp, r, err := apiClient.AgentsAPI.V1AgentsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsGet`: ListAgentsResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsGetRequest struct via the builder pattern


### Return type

[**ListAgentsResponse**](ListAgentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1AgentsPost

> AgentCreateResponse V1AgentsPost(ctx).CreateAgentRequest(createAgentRequest).Execute()





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
	createAgentRequest := *openapiclient.NewCreateAgentRequest(*openapiclient.NewAgentConfig("Model_example", "Instructions_example")) // CreateAgentRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AgentsAPI.V1AgentsPost(context.Background()).CreateAgentRequest(createAgentRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AgentsAPI.V1AgentsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1AgentsPost`: AgentCreateResponse
	fmt.Fprintf(os.Stdout, "Response from `AgentsAPI.V1AgentsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1AgentsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAgentRequest** | [**CreateAgentRequest**](CreateAgentRequest.md) |  | 

### Return type

[**AgentCreateResponse**](AgentCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

