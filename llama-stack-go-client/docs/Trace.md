# Trace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TraceId** | **string** |  | 
**RootSpanId** | **string** |  | 
**StartTime** | **time.Time** |  | 
**EndTime** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewTrace

`func NewTrace(traceId string, rootSpanId string, startTime time.Time, ) *Trace`

NewTrace instantiates a new Trace object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTraceWithDefaults

`func NewTraceWithDefaults() *Trace`

NewTraceWithDefaults instantiates a new Trace object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTraceId

`func (o *Trace) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *Trace) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *Trace) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.


### GetRootSpanId

`func (o *Trace) GetRootSpanId() string`

GetRootSpanId returns the RootSpanId field if non-nil, zero value otherwise.

### GetRootSpanIdOk

`func (o *Trace) GetRootSpanIdOk() (*string, bool)`

GetRootSpanIdOk returns a tuple with the RootSpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRootSpanId

`func (o *Trace) SetRootSpanId(v string)`

SetRootSpanId sets RootSpanId field to given value.


### GetStartTime

`func (o *Trace) GetStartTime() time.Time`

GetStartTime returns the StartTime field if non-nil, zero value otherwise.

### GetStartTimeOk

`func (o *Trace) GetStartTimeOk() (*time.Time, bool)`

GetStartTimeOk returns a tuple with the StartTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartTime

`func (o *Trace) SetStartTime(v time.Time)`

SetStartTime sets StartTime field to given value.


### GetEndTime

`func (o *Trace) GetEndTime() time.Time`

GetEndTime returns the EndTime field if non-nil, zero value otherwise.

### GetEndTimeOk

`func (o *Trace) GetEndTimeOk() (*time.Time, bool)`

GetEndTimeOk returns a tuple with the EndTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEndTime

`func (o *Trace) SetEndTime(v time.Time)`

SetEndTime sets EndTime field to given value.

### HasEndTime

`func (o *Trace) HasEndTime() bool`

HasEndTime returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


