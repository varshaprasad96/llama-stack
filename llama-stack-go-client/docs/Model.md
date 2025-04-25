# Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Identifier** | **string** |  | 
**ProviderResourceId** | **string** |  | 
**ProviderId** | **string** |  | 
**Type** | **string** |  | [default to "model"]
**Metadata** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 
**ModelType** | [**ModelType**](ModelType.md) |  | 

## Methods

### NewModel

`func NewModel(identifier string, providerResourceId string, providerId string, type_ string, metadata map[string]AppendRowsRequestRowsInnerValue, modelType ModelType, ) *Model`

NewModel instantiates a new Model object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewModelWithDefaults

`func NewModelWithDefaults() *Model`

NewModelWithDefaults instantiates a new Model object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdentifier

`func (o *Model) GetIdentifier() string`

GetIdentifier returns the Identifier field if non-nil, zero value otherwise.

### GetIdentifierOk

`func (o *Model) GetIdentifierOk() (*string, bool)`

GetIdentifierOk returns a tuple with the Identifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifier

`func (o *Model) SetIdentifier(v string)`

SetIdentifier sets Identifier field to given value.


### GetProviderResourceId

`func (o *Model) GetProviderResourceId() string`

GetProviderResourceId returns the ProviderResourceId field if non-nil, zero value otherwise.

### GetProviderResourceIdOk

`func (o *Model) GetProviderResourceIdOk() (*string, bool)`

GetProviderResourceIdOk returns a tuple with the ProviderResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderResourceId

`func (o *Model) SetProviderResourceId(v string)`

SetProviderResourceId sets ProviderResourceId field to given value.


### GetProviderId

`func (o *Model) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *Model) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *Model) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetType

`func (o *Model) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Model) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Model) SetType(v string)`

SetType sets Type field to given value.


### GetMetadata

`func (o *Model) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Model) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Model) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.


### GetModelType

`func (o *Model) GetModelType() ModelType`

GetModelType returns the ModelType field if non-nil, zero value otherwise.

### GetModelTypeOk

`func (o *Model) GetModelTypeOk() (*ModelType, bool)`

GetModelTypeOk returns a tuple with the ModelType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModelType

`func (o *Model) SetModelType(v ModelType)`

SetModelType sets ModelType field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


