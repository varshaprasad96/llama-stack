# StructuredLogPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "span_start"]
**Name** | **string** |  | 
**ParentSpanId** | Pointer to **string** |  | [optional] 
**Status** | [**SpanStatus**](SpanStatus.md) |  | 

## Methods

### NewStructuredLogPayload

`func NewStructuredLogPayload(type_ string, name string, status SpanStatus, ) *StructuredLogPayload`

NewStructuredLogPayload instantiates a new StructuredLogPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStructuredLogPayloadWithDefaults

`func NewStructuredLogPayloadWithDefaults() *StructuredLogPayload`

NewStructuredLogPayloadWithDefaults instantiates a new StructuredLogPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *StructuredLogPayload) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *StructuredLogPayload) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *StructuredLogPayload) SetType(v string)`

SetType sets Type field to given value.


### GetName

`func (o *StructuredLogPayload) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *StructuredLogPayload) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *StructuredLogPayload) SetName(v string)`

SetName sets Name field to given value.


### GetParentSpanId

`func (o *StructuredLogPayload) GetParentSpanId() string`

GetParentSpanId returns the ParentSpanId field if non-nil, zero value otherwise.

### GetParentSpanIdOk

`func (o *StructuredLogPayload) GetParentSpanIdOk() (*string, bool)`

GetParentSpanIdOk returns a tuple with the ParentSpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSpanId

`func (o *StructuredLogPayload) SetParentSpanId(v string)`

SetParentSpanId sets ParentSpanId field to given value.

### HasParentSpanId

`func (o *StructuredLogPayload) HasParentSpanId() bool`

HasParentSpanId returns a boolean if a field has been set.

### GetStatus

`func (o *StructuredLogPayload) GetStatus() SpanStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *StructuredLogPayload) GetStatusOk() (*SpanStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *StructuredLogPayload) SetStatus(v SpanStatus)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


