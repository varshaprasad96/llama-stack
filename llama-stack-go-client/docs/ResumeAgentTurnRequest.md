# ResumeAgentTurnRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ToolResponses** | [**[]ToolResponse**](ToolResponse.md) | The tool call responses to resume the turn with. | 
**Stream** | Pointer to **bool** | Whether to stream the response. | [optional] 

## Methods

### NewResumeAgentTurnRequest

`func NewResumeAgentTurnRequest(toolResponses []ToolResponse, ) *ResumeAgentTurnRequest`

NewResumeAgentTurnRequest instantiates a new ResumeAgentTurnRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResumeAgentTurnRequestWithDefaults

`func NewResumeAgentTurnRequestWithDefaults() *ResumeAgentTurnRequest`

NewResumeAgentTurnRequestWithDefaults instantiates a new ResumeAgentTurnRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetToolResponses

`func (o *ResumeAgentTurnRequest) GetToolResponses() []ToolResponse`

GetToolResponses returns the ToolResponses field if non-nil, zero value otherwise.

### GetToolResponsesOk

`func (o *ResumeAgentTurnRequest) GetToolResponsesOk() (*[]ToolResponse, bool)`

GetToolResponsesOk returns a tuple with the ToolResponses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolResponses

`func (o *ResumeAgentTurnRequest) SetToolResponses(v []ToolResponse)`

SetToolResponses sets ToolResponses field to given value.


### GetStream

`func (o *ResumeAgentTurnRequest) GetStream() bool`

GetStream returns the Stream field if non-nil, zero value otherwise.

### GetStreamOk

`func (o *ResumeAgentTurnRequest) GetStreamOk() (*bool, bool)`

GetStreamOk returns a tuple with the Stream field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStream

`func (o *ResumeAgentTurnRequest) SetStream(v bool)`

SetStream sets Stream field to given value.

### HasStream

`func (o *ResumeAgentTurnRequest) HasStream() bool`

HasStream returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


