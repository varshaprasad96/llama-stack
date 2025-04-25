# SpanStartPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "span_start"]
**Name** | **string** |  | 
**ParentSpanId** | Pointer to **string** |  | [optional] 

## Methods

### NewSpanStartPayload

`func NewSpanStartPayload(type_ string, name string, ) *SpanStartPayload`

NewSpanStartPayload instantiates a new SpanStartPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpanStartPayloadWithDefaults

`func NewSpanStartPayloadWithDefaults() *SpanStartPayload`

NewSpanStartPayloadWithDefaults instantiates a new SpanStartPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *SpanStartPayload) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SpanStartPayload) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SpanStartPayload) SetType(v string)`

SetType sets Type field to given value.


### GetName

`func (o *SpanStartPayload) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SpanStartPayload) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SpanStartPayload) SetName(v string)`

SetName sets Name field to given value.


### GetParentSpanId

`func (o *SpanStartPayload) GetParentSpanId() string`

GetParentSpanId returns the ParentSpanId field if non-nil, zero value otherwise.

### GetParentSpanIdOk

`func (o *SpanStartPayload) GetParentSpanIdOk() (*string, bool)`

GetParentSpanIdOk returns a tuple with the ParentSpanId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParentSpanId

`func (o *SpanStartPayload) SetParentSpanId(v string)`

SetParentSpanId sets ParentSpanId field to given value.

### HasParentSpanId

`func (o *SpanStartPayload) HasParentSpanId() bool`

HasParentSpanId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


