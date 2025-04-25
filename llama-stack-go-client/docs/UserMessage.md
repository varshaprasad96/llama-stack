# UserMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;user\&quot; to identify this as a user message | [default to "user"]
**Content** | [**InterleavedContent**](InterleavedContent.md) | The content of the message, which can include text and other media | 
**Context** | Pointer to [**InterleavedContent**](InterleavedContent.md) | (Optional) This field is used internally by Llama Stack to pass RAG context. This field may be removed in the API in the future. | [optional] 

## Methods

### NewUserMessage

`func NewUserMessage(role string, content InterleavedContent, ) *UserMessage`

NewUserMessage instantiates a new UserMessage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserMessageWithDefaults

`func NewUserMessageWithDefaults() *UserMessage`

NewUserMessageWithDefaults instantiates a new UserMessage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *UserMessage) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *UserMessage) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *UserMessage) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *UserMessage) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *UserMessage) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *UserMessage) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.


### GetContext

`func (o *UserMessage) GetContext() InterleavedContent`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *UserMessage) GetContextOk() (*InterleavedContent, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *UserMessage) SetContext(v InterleavedContent)`

SetContext sets Context field to given value.

### HasContext

`func (o *UserMessage) HasContext() bool`

HasContext returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


