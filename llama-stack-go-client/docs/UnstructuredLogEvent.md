# UnstructuredLogEvent

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

## Methods

### NewUnstructuredLogEvent

`func NewUnstructuredLogEvent(traceId string, spanId string, timestamp time.Time, type_ string, message string, severity LogSeverity, ) *UnstructuredLogEvent`

NewUnstructuredLogEvent instantiates a new UnstructuredLogEvent object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUnstructuredLogEventWithDefaults

`func NewUnstructuredLogEventWithDefaults() *UnstructuredLogEvent`

NewUnstructuredLogEventWithDefaults instantiates a new UnstructuredLogEvent object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTraceId

`func (o *UnstructuredLogEvent) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *UnstructuredLogEvent) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *UnstructuredLogEvent) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.


### GetSpanId

`func (o *UnstructuredLogEvent) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *UnstructuredLogEvent) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *UnstructuredLogEvent) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.


### GetTimestamp

`func (o *UnstructuredLogEvent) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *UnstructuredLogEvent) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *UnstructuredLogEvent) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetAttributes

`func (o *UnstructuredLogEvent) GetAttributes() map[string]ToolCallArgumentsOneOfValueOneOfInner`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *UnstructuredLogEvent) GetAttributesOk() (*map[string]ToolCallArgumentsOneOfValueOneOfInner, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *UnstructuredLogEvent) SetAttributes(v map[string]ToolCallArgumentsOneOfValueOneOfInner)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *UnstructuredLogEvent) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.

### GetType

`func (o *UnstructuredLogEvent) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *UnstructuredLogEvent) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *UnstructuredLogEvent) SetType(v string)`

SetType sets Type field to given value.


### GetMessage

`func (o *UnstructuredLogEvent) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *UnstructuredLogEvent) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *UnstructuredLogEvent) SetMessage(v string)`

SetMessage sets Message field to given value.


### GetSeverity

`func (o *UnstructuredLogEvent) GetSeverity() LogSeverity`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *UnstructuredLogEvent) GetSeverityOk() (*LogSeverity, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *UnstructuredLogEvent) SetSeverity(v LogSeverity)`

SetSeverity sets Severity field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


