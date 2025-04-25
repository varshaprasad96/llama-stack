# RouteInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Route** | **string** |  | 
**Method** | **string** |  | 
**ProviderTypes** | **[]string** |  | 

## Methods

### NewRouteInfo

`func NewRouteInfo(route string, method string, providerTypes []string, ) *RouteInfo`

NewRouteInfo instantiates a new RouteInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRouteInfoWithDefaults

`func NewRouteInfoWithDefaults() *RouteInfo`

NewRouteInfoWithDefaults instantiates a new RouteInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRoute

`func (o *RouteInfo) GetRoute() string`

GetRoute returns the Route field if non-nil, zero value otherwise.

### GetRouteOk

`func (o *RouteInfo) GetRouteOk() (*string, bool)`

GetRouteOk returns a tuple with the Route field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoute

`func (o *RouteInfo) SetRoute(v string)`

SetRoute sets Route field to given value.


### GetMethod

`func (o *RouteInfo) GetMethod() string`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *RouteInfo) GetMethodOk() (*string, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *RouteInfo) SetMethod(v string)`

SetMethod sets Method field to given value.


### GetProviderTypes

`func (o *RouteInfo) GetProviderTypes() []string`

GetProviderTypes returns the ProviderTypes field if non-nil, zero value otherwise.

### GetProviderTypesOk

`func (o *RouteInfo) GetProviderTypesOk() (*[]string, bool)`

GetProviderTypesOk returns a tuple with the ProviderTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderTypes

`func (o *RouteInfo) SetProviderTypes(v []string)`

SetProviderTypes sets ProviderTypes field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


