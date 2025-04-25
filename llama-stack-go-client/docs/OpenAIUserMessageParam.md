# OpenAIUserMessageParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;user\&quot; to identify this as a user message | [default to "user"]
**Content** | [**OpenAIUserMessageParamContent**](OpenAIUserMessageParamContent.md) |  | 
**Name** | Pointer to **string** | (Optional) The name of the user message participant. | [optional] 

## Methods

### NewOpenAIUserMessageParam

`func NewOpenAIUserMessageParam(role string, content OpenAIUserMessageParamContent, ) *OpenAIUserMessageParam`

NewOpenAIUserMessageParam instantiates a new OpenAIUserMessageParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIUserMessageParamWithDefaults

`func NewOpenAIUserMessageParamWithDefaults() *OpenAIUserMessageParam`

NewOpenAIUserMessageParamWithDefaults instantiates a new OpenAIUserMessageParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *OpenAIUserMessageParam) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *OpenAIUserMessageParam) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *OpenAIUserMessageParam) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *OpenAIUserMessageParam) GetContent() OpenAIUserMessageParamContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAIUserMessageParam) GetContentOk() (*OpenAIUserMessageParamContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAIUserMessageParam) SetContent(v OpenAIUserMessageParamContent)`

SetContent sets Content field to given value.


### GetName

`func (o *OpenAIUserMessageParam) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *OpenAIUserMessageParam) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *OpenAIUserMessageParam) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *OpenAIUserMessageParam) HasName() bool`

HasName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


