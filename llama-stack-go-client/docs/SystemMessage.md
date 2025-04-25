# SystemMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;system\&quot; to identify this as a system message | [default to "system"]
**Content** | [**InterleavedContent**](InterleavedContent.md) | The content of the \&quot;system prompt\&quot;. If multiple system messages are provided, they are concatenated. The underlying Llama Stack code may also add other system messages (for example, for formatting tool definitions). | 

## Methods

### NewSystemMessage

`func NewSystemMessage(role string, content InterleavedContent, ) *SystemMessage`

NewSystemMessage instantiates a new SystemMessage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemMessageWithDefaults

`func NewSystemMessageWithDefaults() *SystemMessage`

NewSystemMessageWithDefaults instantiates a new SystemMessage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *SystemMessage) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *SystemMessage) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *SystemMessage) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *SystemMessage) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *SystemMessage) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *SystemMessage) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


