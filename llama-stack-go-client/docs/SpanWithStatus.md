# SpanWithStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SpanId** | **string** |  | 
**TraceId** | **string** |  | 
**ParentSpanId** | Pointer to **string** |  | [optional] 
**Name** | **string** |  | 
**StartTime** | **time.Time** |  | 
**EndTime** | Pointer to **time.Time** |  | [optional] 
**Attributes** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 
**Status** | Pointer to [**SpanStatus**](SpanStatus.md) |  | [optional] 

## Methods

### NewSpanWithStatus

`func NewSpanWithStatus(spanId string, traceId string, name string, startTime time.Time, ) *SpanWithStatus`

NewSpanWithStatus instantiates a new SpanWithStatus object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpanWithStatusWithDefaults

`func NewSpanWithStatusWithDefaults() *SpanWithStatus`

NewSpanWithStatusWithDefaults instantiates a new SpanWithStatus object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpanId

`func (o *SpanWithStatus) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *SpanWithStatus) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *SpanWithStatus) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.


### GetTraceId

`func (o *SpanWithStatus) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *SpanWithStatus) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *SpanWithStatus) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.


### GetParentSpanId

`func (o *SpanWithStatus) GetParentSpanId() string`

GetParentSpanId returns the ParentSpanId field if non-nil, zero value otherwise.

### GetParentSpanIdOk

`func (o *SpanWithStatus) GetParentSpanIdOk() (*string, bool)`

GetParentSpanIdOk returns a tuple with the ParentSpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSpanId

`func (o *SpanWithStatus) SetParentSpanId(v string)`

SetParentSpanId sets ParentSpanId field to given value.

### HasParentSpanId

`func (o *SpanWithStatus) HasParentSpanId() bool`

HasParentSpanId returns a boolean if a field has been set.

### GetName

`func (o *SpanWithStatus) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SpanWithStatus) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SpanWithStatus) SetName(v string)`

SetName sets Name field to given value.


### GetStartTime

`func (o *SpanWithStatus) GetStartTime() time.Time`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *SpanWithStatus) GetStartTimeOk() (*time.Time, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *SpanWithStatus) SetStartTime(v time.Time)`

SetStartTime sets StartTime field to given value.


### GetEndTime

`func (o *SpanWithStatus) GetEndTime() time.Time`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *SpanWithStatus) GetEndTimeOk() (*time.Time, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndTime

`func (o *SpanWithStatus) SetEndTime(v time.Time)`

SetEndTime sets EndTime field to given value.

### HasEndTime

`func (o *SpanWithStatus) HasEndTime() bool`

HasEndTime returns a boolean if a field has been set.

### GetAttributes

`func (o *SpanWithStatus) GetAttributes() map[string]AppendRowsRequestRowsInnerValue`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *SpanWithStatus) GetAttributesOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *SpanWithStatus) SetAttributes(v map[string]AppendRowsRequestRowsInnerValue)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *SpanWithStatus) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.

### GetStatus

`func (o *SpanWithStatus) GetStatus() SpanStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SpanWithStatus) GetStatusOk() (*SpanStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SpanWithStatus) SetStatus(v SpanStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *SpanWithStatus) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


