# MetricEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TraceId** | **string** |  | 
**SpanId** | **string** |  | 
**Timestamp** | **time.Time** |  | 
**Attributes** | Pointer to [**map[string]ToolCallArgumentsOneOfValueOneOfInner**](ToolCallArgumentsOneOfValueOneOfInner.md) |  | [optional] 
**Type** | **string** |  | [default to "metric"]
**Metric** | **string** |  | 
**Value** | [**MetricInResponseValue**](MetricInResponseValue.md) |  | 
**Unit** | **string** |  | 

## Methods

### NewMetricEvent

`func NewMetricEvent(traceId string, spanId string, timestamp time.Time, type_ string, metric string, value MetricInResponseValue, unit string, ) *MetricEvent`

NewMetricEvent instantiates a new MetricEvent object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMetricEventWithDefaults

`func NewMetricEventWithDefaults() *MetricEvent`

NewMetricEventWithDefaults instantiates a new MetricEvent object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTraceId

`func (o *MetricEvent) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *MetricEvent) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *MetricEvent) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.


### GetSpanId

`func (o *MetricEvent) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *MetricEvent) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *MetricEvent) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.


### GetTimestamp

`func (o *MetricEvent) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *MetricEvent) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *MetricEvent) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetAttributes

`func (o *MetricEvent) GetAttributes() map[string]ToolCallArgumentsOneOfValueOneOfInner`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *MetricEvent) GetAttributesOk() (*map[string]ToolCallArgumentsOneOfValueOneOfInner, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *MetricEvent) SetAttributes(v map[string]ToolCallArgumentsOneOfValueOneOfInner)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *MetricEvent) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.

### GetType

`func (o *MetricEvent) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *MetricEvent) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *MetricEvent) SetType(v string)`

SetType sets Type field to given value.


### GetMetric

`func (o *MetricEvent) GetMetric() string`

GetMetric returns the Metric field if non-nil, zero value otherwise.

### GetMetricOk

`func (o *MetricEvent) GetMetricOk() (*string, bool)`

GetMetricOk returns a tuple with the Metric field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetric

`func (o *MetricEvent) SetMetric(v string)`

SetMetric sets Metric field to given value.


### GetValue

`func (o *MetricEvent) GetValue() MetricInResponseValue`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *MetricEvent) GetValueOk() (*MetricInResponseValue, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *MetricEvent) SetValue(v MetricInResponseValue)`

SetValue sets Value field to given value.


### GetUnit

`func (o *MetricEvent) GetUnit() string`

GetUnit returns the Unit field if non-nil, zero value otherwise.

### GetUnitOk

`func (o *MetricEvent) GetUnitOk() (*string, bool)`

GetUnitOk returns a tuple with the Unit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnit

`func (o *MetricEvent) SetUnit(v string)`

SetUnit sets Unit field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


