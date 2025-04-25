# OpenAISystemMessageParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;system\&quot; to identify this as a system message | [default to "system"]
**Content** | [**OpenAISystemMessageParamContent**](OpenAISystemMessageParamContent.md) |  | 
**Name** | Pointer to **string** | (Optional) The name of the system message participant. | [optional] 

## Methods

### NewOpenAISystemMessageParam

`func NewOpenAISystemMessageParam(role string, content OpenAISystemMessageParamContent, ) *OpenAISystemMessageParam`

NewOpenAISystemMessageParam instantiates a new OpenAISystemMessageParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAISystemMessageParamWithDefaults

`func NewOpenAISystemMessageParamWithDefaults() *OpenAISystemMessageParam`

NewOpenAISystemMessageParamWithDefaults instantiates a new OpenAISystemMessageParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *OpenAISystemMessageParam) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *OpenAISystemMessageParam) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *OpenAISystemMessageParam) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *OpenAISystemMessageParam) GetContent() OpenAISystemMessageParamContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAISystemMessageParam) GetContentOk() (*OpenAISystemMessageParamContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAISystemMessageParam) SetContent(v OpenAISystemMessageParamContent)`

SetContent sets Content field to given value.


### GetName

`func (o *OpenAISystemMessageParam) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *OpenAISystemMessageParam) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *OpenAISystemMessageParam) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *OpenAISystemMessageParam) HasName() bool`

HasName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


