# SyntheticDataGenerateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Dialogs** | [**[]Message**](Message.md) |  | 
**FilteringFunction** | **string** | The type of filtering function. | 
**Model** | Pointer to **string** |  | [optional] 

## Methods

### NewSyntheticDataGenerateRequest

`func NewSyntheticDataGenerateRequest(dialogs []Message, filteringFunction string, ) *SyntheticDataGenerateRequest`

NewSyntheticDataGenerateRequest instantiates a new SyntheticDataGenerateRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSyntheticDataGenerateRequestWithDefaults

`func NewSyntheticDataGenerateRequestWithDefaults() *SyntheticDataGenerateRequest`

NewSyntheticDataGenerateRequestWithDefaults instantiates a new SyntheticDataGenerateRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDialogs

`func (o *SyntheticDataGenerateRequest) GetDialogs() []Message`

GetDialogs returns the Dialogs field if non-nil, zero value otherwise.

### GetDialogsOk

`func (o *SyntheticDataGenerateRequest) GetDialogsOk() (*[]Message, bool)`

GetDialogsOk returns a tuple with the Dialogs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDialogs

`func (o *SyntheticDataGenerateRequest) SetDialogs(v []Message)`

SetDialogs sets Dialogs field to given value.


### GetFilteringFunction

`func (o *SyntheticDataGenerateRequest) GetFilteringFunction() string`

GetFilteringFunction returns the FilteringFunction field if non-nil, zero value otherwise.

### GetFilteringFunctionOk

`func (o *SyntheticDataGenerateRequest) GetFilteringFunctionOk() (*string, bool)`

GetFilteringFunctionOk returns a tuple with the FilteringFunction field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFilteringFunction

`func (o *SyntheticDataGenerateRequest) SetFilteringFunction(v string)`

SetFilteringFunction sets FilteringFunction field to given value.


### GetModel

`func (o *SyntheticDataGenerateRequest) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *SyntheticDataGenerateRequest) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *SyntheticDataGenerateRequest) SetModel(v string)`

SetModel sets Model field to given value.

### HasModel

`func (o *SyntheticDataGenerateRequest) HasModel() bool`

HasModel returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


