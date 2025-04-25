# SpanEndPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "span_end"]
**Status** | [**SpanStatus**](SpanStatus.md) |  | 

## Methods

### NewSpanEndPayload

`func NewSpanEndPayload(type_ string, status SpanStatus, ) *SpanEndPayload`

NewSpanEndPayload instantiates a new SpanEndPayload object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSpanEndPayloadWithDefaults

`func NewSpanEndPayloadWithDefaults() *SpanEndPayload`

NewSpanEndPayloadWithDefaults instantiates a new SpanEndPayload object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *SpanEndPayload) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SpanEndPayload) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SpanEndPayload) SetType(v string)`

SetType sets Type field to given value.


### GetStatus

`func (o *SpanEndPayload) GetStatus() SpanStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SpanEndPayload) GetStatusOk() (*SpanStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SpanEndPayload) SetStatus(v SpanStatus)`

SetStatus sets Status field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


