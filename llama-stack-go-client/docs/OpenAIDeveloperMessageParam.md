# OpenAIDeveloperMessageParam

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Role** | **string** | Must be \&quot;developer\&quot; to identify this as a developer message | [default to "developer"]
**Content** | [**OpenAIDeveloperMessageParamContent**](OpenAIDeveloperMessageParamContent.md) |  | 
**Name** | Pointer to **string** | (Optional) The name of the developer message participant. | [optional] 

## Methods

### NewOpenAIDeveloperMessageParam

`func NewOpenAIDeveloperMessageParam(role string, content OpenAIDeveloperMessageParamContent, ) *OpenAIDeveloperMessageParam`

NewOpenAIDeveloperMessageParam instantiates a new OpenAIDeveloperMessageParam object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIDeveloperMessageParamWithDefaults

`func NewOpenAIDeveloperMessageParamWithDefaults() *OpenAIDeveloperMessageParam`

NewOpenAIDeveloperMessageParamWithDefaults instantiates a new OpenAIDeveloperMessageParam object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRole

`func (o *OpenAIDeveloperMessageParam) GetRole() string`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *OpenAIDeveloperMessageParam) GetRoleOk() (*string, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *OpenAIDeveloperMessageParam) SetRole(v string)`

SetRole sets Role field to given value.


### GetContent

`func (o *OpenAIDeveloperMessageParam) GetContent() OpenAIDeveloperMessageParamContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *OpenAIDeveloperMessageParam) GetContentOk() (*OpenAIDeveloperMessageParamContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *OpenAIDeveloperMessageParam) SetContent(v OpenAIDeveloperMessageParamContent)`

SetContent sets Content field to given value.


### GetName

`func (o *OpenAIDeveloperMessageParam) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *OpenAIDeveloperMessageParam) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *OpenAIDeveloperMessageParam) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *OpenAIDeveloperMessageParam) HasName() bool`

HasName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


