# StructuredLogEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TraceId** | **string** |  | 
**SpanId** | **string** |  | 
**Timestamp** | **time.Time** |  | 
**Attributes** | Pointer to [**map[string]ToolCallArgumentsOneOfValueOneOfInner**](ToolCallArgumentsOneOfValueOneOfInner.md) |  | [optional] 
**Type** | **string** |  | [default to "structured_log"]
**Payload** | [**StructuredLogPayload**](StructuredLogPayload.md) |  | 

## Methods

### NewStructuredLogEvent

`func NewStructuredLogEvent(traceId string, spanId string, timestamp time.Time, type_ string, payload StructuredLogPayload, ) *StructuredLogEvent`

NewStructuredLogEvent instantiates a new StructuredLogEvent object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStructuredLogEventWithDefaults

`func NewStructuredLogEventWithDefaults() *StructuredLogEvent`

NewStructuredLogEventWithDefaults instantiates a new StructuredLogEvent object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTraceId

`func (o *StructuredLogEvent) GetTraceId() string`

GetTraceId returns the TraceId field if non-nil, zero value otherwise.

### GetTraceIdOk

`func (o *StructuredLogEvent) GetTraceIdOk() (*string, bool)`

GetTraceIdOk returns a tuple with the TraceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTraceId

`func (o *StructuredLogEvent) SetTraceId(v string)`

SetTraceId sets TraceId field to given value.


### GetSpanId

`func (o *StructuredLogEvent) GetSpanId() string`

GetSpanId returns the SpanId field if non-nil, zero value otherwise.

### GetSpanIdOk

`func (o *StructuredLogEvent) GetSpanIdOk() (*string, bool)`

GetSpanIdOk returns a tuple with the SpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpanId

`func (o *StructuredLogEvent) SetSpanId(v string)`

SetSpanId sets SpanId field to given value.


### GetTimestamp

`func (o *StructuredLogEvent) GetTimestamp() time.Time`

GetTimestamp returns the Timestamp field if non-nil, zero value otherwise.

### GetTimestampOk

`func (o *StructuredLogEvent) GetTimestampOk() (*time.Time, bool)`

GetTimestampOk returns a tuple with the Timestamp field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimestamp

`func (o *StructuredLogEvent) SetTimestamp(v time.Time)`

SetTimestamp sets Timestamp field to given value.


### GetAttributes

`func (o *StructuredLogEvent) GetAttributes() map[string]ToolCallArgumentsOneOfValueOneOfInner`

GetAttributes returns the Attributes field if non-nil, zero value otherwise.

### GetAttributesOk

`func (o *StructuredLogEvent) GetAttributesOk() (*map[string]ToolCallArgumentsOneOfValueOneOfInner, bool)`

GetAttributesOk returns a tuple with the Attributes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttributes

`func (o *StructuredLogEvent) SetAttributes(v map[string]ToolCallArgumentsOneOfValueOneOfInner)`

SetAttributes sets Attributes field to given value.

### HasAttributes

`func (o *StructuredLogEvent) HasAttributes() bool`

HasAttributes returns a boolean if a field has been set.

### GetType

`func (o *StructuredLogEvent) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *StructuredLogEvent) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *StructuredLogEvent) SetType(v string)`

SetType sets Type field to given value.


### GetPayload

`func (o *StructuredLogEvent) GetPayload() StructuredLogPayload`

GetPayload returns the Payload field if non-nil, zero value otherwise.

### GetPayloadOk

`func (o *StructuredLogEvent) GetPayloadOk() (*StructuredLogPayload, bool)`

GetPayloadOk returns a tuple with the Payload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayload

`func (o *StructuredLogEvent) SetPayload(v StructuredLogPayload)`

SetPayload sets Payload field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


