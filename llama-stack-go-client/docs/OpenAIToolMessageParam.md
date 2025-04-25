# OpenAIToolMessageParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;tool\&quot; to identify this as a tool response | [default to "tool"]
**ToolCallId** | **string** | Unique identifier for the tool call this response is for | 
**Content** | [**OpenAIToolMessageParamContent**](OpenAIToolMessageParamContent.md) |  | 

## Methods

### NewOpenAIToolMessageParam

`func NewOpenAIToolMessageParam(role string, toolCallId string, content OpenAIToolMessageParamContent, ) *OpenAIToolMessageParam`

NewOpenAIToolMessageParam instantiates a new OpenAIToolMessageParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIToolMessageParamWithDefaults

`func NewOpenAIToolMessageParamWithDefaults() *OpenAIToolMessageParam`

NewOpenAIToolMessageParamWithDefaults instantiates a new OpenAIToolMessageParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *OpenAIToolMessageParam) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *OpenAIToolMessageParam) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *OpenAIToolMessageParam) SetRole(v string)`

SetRole sets Role field to given value.


### GetToolCallId

`func (o *OpenAIToolMessageParam) GetToolCallId() string`

GetToolCallId returns the ToolCallId field if non-nil, zero value otherwise.

### GetToolCallIdOk

`func (o *OpenAIToolMessageParam) GetToolCallIdOk() (*string, bool)`

GetToolCallIdOk returns a tuple with the ToolCallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCallId

`func (o *OpenAIToolMessageParam) SetToolCallId(v string)`

SetToolCallId sets ToolCallId field to given value.


### GetContent

`func (o *OpenAIToolMessageParam) GetContent() OpenAIToolMessageParamContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAIToolMessageParam) GetContentOk() (*OpenAIToolMessageParamContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAIToolMessageParam) SetContent(v OpenAIToolMessageParamContent)`

SetContent sets Content field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


