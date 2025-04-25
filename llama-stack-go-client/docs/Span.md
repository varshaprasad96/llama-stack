# Span

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

## Methods

### NewSpan

`func NewSpan(spanId string, traceId string, name string, startTime time.Time, ) *Span`

NewSpan instantiates a new Span object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpanWithDefaults

`func NewSpanWithDefaults() *Span`

NewSpanWithDefaults instantiates a new Span object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSpanId

`func (o *Span) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *Span) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *Span) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.


### GetTraceId

`func (o *Span) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *Span) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *Span) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.


### GetParentSpanId

`func (o *Span) GetParentSpanId() string`

GetParentSpanId returns the ParentSpanId field if non-nil, zero value otherwise.

### GetParentSpanIdOk

`func (o *Span) GetParentSpanIdOk() (*string, bool)`

GetParentSpanIdOk returns a tuple with the ParentSpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSpanId

`func (o *Span) SetParentSpanId(v string)`

SetParentSpanId sets ParentSpanId field to given value.

### HasParentSpanId

`func (o *Span) HasParentSpanId() bool`

HasParentSpanId returns a boolean if a field has been set.

### GetName

`func (o *Span) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Span) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Span) SetName(v string)`

SetName sets Name field to given value.


### GetStartTime

`func (o *Span) GetStartTime() time.Time`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *Span) GetStartTimeOk() (*time.Time, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *Span) SetStartTime(v time.Time)`

SetStartTime sets StartTime field to given value.


### GetEndTime

`func (o *Span) GetEndTime() time.Time`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *Span) GetEndTimeOk() (*time.Time, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndTime

`func (o *Span) SetEndTime(v time.Time)`

SetEndTime sets EndTime field to given value.

### HasEndTime

`func (o *Span) HasEndTime() bool`

HasEndTime returns a boolean if a field has been set.

### GetAttributes

`func (o *Span) GetAttributes() map[string]AppendRowsRequestRowsInnerValue`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *Span) GetAttributesOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *Span) SetAttributes(v map[string]AppendRowsRequestRowsInnerValue)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *Span) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


