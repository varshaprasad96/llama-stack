# QuerySpanTreeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Data** | [**map[string]SpanWithStatus**](SpanWithStatus.md) |  | 

## Methods

### NewQuerySpanTreeResponse

`func NewQuerySpanTreeResponse(data map[string]SpanWithStatus, ) *QuerySpanTreeResponse`

NewQuerySpanTreeResponse instantiates a new QuerySpanTreeResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewQuerySpanTreeResponseWithDefaults

`func NewQuerySpanTreeResponseWithDefaults() *QuerySpanTreeResponse`

NewQuerySpanTreeResponseWithDefaults instantiates a new QuerySpanTreeResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetData

`func (o *QuerySpanTreeResponse) GetData() map[string]SpanWithStatus`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *QuerySpanTreeResponse) GetDataOk() (*map[string]SpanWithStatus, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *QuerySpanTreeResponse) SetData(v map[string]SpanWithStatus)`

SetData sets Data field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


