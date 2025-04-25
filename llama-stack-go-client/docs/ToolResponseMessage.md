# ToolResponseMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;tool\&quot; to identify this as a tool response | [default to "tool"]
**CallId** | **string** | Unique identifier for the tool call this response is for | 
**Content** | [**InterleavedContent**](InterleavedContent.md) | The response content from the tool | 

## Methods

### NewToolResponseMessage

`func NewToolResponseMessage(role string, callId string, content InterleavedContent, ) *ToolResponseMessage`

NewToolResponseMessage instantiates a new ToolResponseMessage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolResponseMessageWithDefaults

`func NewToolResponseMessageWithDefaults() *ToolResponseMessage`

NewToolResponseMessageWithDefaults instantiates a new ToolResponseMessage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *ToolResponseMessage) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *ToolResponseMessage) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *ToolResponseMessage) SetRole(v string)`

SetRole sets Role field to given value.


### GetCallId

`func (o *ToolResponseMessage) GetCallId() string`

GetCallId returns the CallId field if non-nil, zero value otherwise.

### GetCallIdOk

`func (o *ToolResponseMessage) GetCallIdOk() (*string, bool)`

GetCallIdOk returns a tuple with the CallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallId

`func (o *ToolResponseMessage) SetCallId(v string)`

SetCallId sets CallId field to given value.


### GetContent

`func (o *ToolResponseMessage) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *ToolResponseMessage) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *ToolResponseMessage) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


