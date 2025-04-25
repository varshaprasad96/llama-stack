# Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TraceId** | **string** |  | 
**SpanId** | **string** |  | 
**Timestamp** | **time.Time** |  | 
**Attributes** | Pointer to [**map[string]ToolCallArgumentsOneOfValueOneOfInner**](ToolCallArgumentsOneOfValueOneOfInner.md) |  | [optional] 
**Type** | **string** |  | [default to "unstructured_log"]
**Message** | **string** |  | 
**Severity** | [**LogSeverity**](LogSeverity.md) |  | 
**Metric** | **string** |  | 
**Value** | [**MetricInResponseValue**](MetricInResponseValue.md) |  | 
**Unit** | **string** |  | 
**Payload** | [**StructuredLogPayload**](StructuredLogPayload.md) |  | 

## Methods

### NewEvent

`func NewEvent(traceId string, spanId string, timestamp time.Time, type_ string, message string, severity LogSeverity, metric string, value MetricInResponseValue, unit string, payload StructuredLogPayload, ) *Event`

NewEvent instantiates a new Event object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEventWithDefaults

`func NewEventWithDefaults() *Event`

NewEventWithDefaults instantiates a new Event object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTraceId

`func (o *Event) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *Event) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *Event) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.


### GetSpanId

`func (o *Event) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *Event) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *Event) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.


### GetTimestamp

`func (o *Event) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *Event) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *Event) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetAttributes

`func (o *Event) GetAttributes() map[string]ToolCallArgumentsOneOfValueOneOfInner`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *Event) GetAttributesOk() (*map[string]ToolCallArgumentsOneOfValueOneOfInner, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *Event) SetAttributes(v map[string]ToolCallArgumentsOneOfValueOneOfInner)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *Event) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.

### GetType

`func (o *Event) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Event) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Event) SetType(v string)`

SetType sets Type field to given value.


### GetMessage

`func (o *Event) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *Event) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *Event) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetSeverity

`func (o *Event) GetSeverity() LogSeverity`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *Event) GetSeverityOk() (*LogSeverity, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *Event) SetSeverity(v LogSeverity)`

SetSeverity sets Severity field to given value.


### GetMetric

`func (o *Event) GetMetric() string`

GetMetric returns the Metric field if non-nil, zero value otherwise.

### GetMetricOk

`func (o *Event) GetMetricOk() (*string, bool)`

GetMetricOk returns a tuple with the Metric field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetric

`func (o *Event) SetMetric(v string)`

SetMetric sets Metric field to given value.


### GetValue

`func (o *Event) GetValue() MetricInResponseValue`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *Event) GetValueOk() (*MetricInResponseValue, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *Event) SetValue(v MetricInResponseValue)`

SetValue sets Value field to given value.


### GetUnit

`func (o *Event) GetUnit() string`

GetUnit returns the Unit field if non-nil, zero value otherwise.

### GetUnitOk

`func (o *Event) GetUnitOk() (*string, bool)`

GetUnitOk returns a tuple with the Unit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUnit

`func (o *Event) SetUnit(v string)`

SetUnit sets Unit field to given value.


### GetPayload

`func (o *Event) GetPayload() StructuredLogPayload`

GetPayload returns the Payload field if non-nil, zero value otherwise.

### GetPayloadOk

`func (o *Event) GetPayloadOk() (*StructuredLogPayload, bool)`

GetPayloadOk returns a tuple with the Payload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayload

`func (o *Event) SetPayload(v StructuredLogPayload)`

SetPayload sets Payload field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


