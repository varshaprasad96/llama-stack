# MetricInResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metric** | **string** |  | 
**Value** | [**MetricInResponseValue**](MetricInResponseValue.md) |  | 
**Unit** | Pointer to **string** |  | [optional] 

## Methods

### NewMetricInResponse

`func NewMetricInResponse(metric string, value MetricInResponseValue, ) *MetricInResponse`

NewMetricInResponse instantiates a new MetricInResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMetricInResponseWithDefaults

`func NewMetricInResponseWithDefaults() *MetricInResponse`

NewMetricInResponseWithDefaults instantiates a new MetricInResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetric

`func (o *MetricInResponse) GetMetric() string`

GetMetric returns the Metric field if non-nil, zero value otherwise.

### GetMetricOk

`func (o *MetricInResponse) GetMetricOk() (*string, bool)`

GetMetricOk returns a tuple with the Metric field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetric

`func (o *MetricInResponse) SetMetric(v string)`

SetMetric sets Metric field to given value.


### GetValue

`func (o *MetricInResponse) GetValue() MetricInResponseValue`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *MetricInResponse) GetValueOk() (*MetricInResponseValue, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *MetricInResponse) SetValue(v MetricInResponseValue)`

SetValue sets Value field to given value.


### GetUnit

`func (o *MetricInResponse) GetUnit() string`

GetUnit returns the Unit field if non-nil, zero value otherwise.

### GetUnitOk

`func (o *MetricInResponse) GetUnitOk() (*string, bool)`

GetUnitOk returns a tuple with the Unit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnit

`func (o *MetricInResponse) SetUnit(v string)`

SetUnit sets Unit field to given value.

### HasUnit

`func (o *MetricInResponse) HasUnit() bool`

HasUnit returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


