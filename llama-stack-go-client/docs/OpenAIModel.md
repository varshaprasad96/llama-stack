# OpenAIModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Object** | **string** |  | [default to "model"]
**Created** | **int32** |  | 
**OwnedBy** | **string** |  | 

## Methods

### NewOpenAIModel

`func NewOpenAIModel(id string, object string, created int32, ownedBy string, ) *OpenAIModel`

NewOpenAIModel instantiates a new OpenAIModel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIModelWithDefaults

`func NewOpenAIModelWithDefaults() *OpenAIModel`

NewOpenAIModelWithDefaults instantiates a new OpenAIModel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *OpenAIModel) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *OpenAIModel) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *OpenAIModel) SetId(v string)`

SetId sets Id field to given value.


### GetObject

`func (o *OpenAIModel) GetObject() string`

GetObject returns the Object field if non-nil, zero value otherwise.

### GetObjectOk

`func (o *OpenAIModel) GetObjectOk() (*string, bool)`

GetObjectOk returns a tuple with the Object field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObject

`func (o *OpenAIModel) SetObject(v string)`

SetObject sets Object field to given value.


### GetCreated

`func (o *OpenAIModel) GetCreated() int32`

GetCreated returns the Created field if non-nil, zero value otherwise.

### GetCreatedOk

`func (o *OpenAIModel) GetCreatedOk() (*int32, bool)`

GetCreatedOk returns a tuple with the Created field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreated

`func (o *OpenAIModel) SetCreated(v int32)`

SetCreated sets Created field to given value.


### GetOwnedBy

`func (o *OpenAIModel) GetOwnedBy() string`

GetOwnedBy returns the OwnedBy field if non-nil, zero value otherwise.

### GetOwnedByOk

`func (o *OpenAIModel) GetOwnedByOk() (*string, bool)`

GetOwnedByOk returns a tuple with the OwnedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwnedBy

`func (o *OpenAIModel) SetOwnedBy(v string)`

SetOwnedBy sets OwnedBy field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


