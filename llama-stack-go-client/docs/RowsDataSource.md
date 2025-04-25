# RowsDataSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "rows"]
**Rows** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | The dataset is stored in rows. E.g. - [ {\&quot;messages\&quot;: [{\&quot;role\&quot;: \&quot;user\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}, {\&quot;role\&quot;: \&quot;assistant\&quot;, \&quot;content\&quot;: \&quot;Hello, world!\&quot;}]} ] | 

## Methods

### NewRowsDataSource

`func NewRowsDataSource(type_ string, rows []map[string]AppendRowsRequestRowsInnerValue, ) *RowsDataSource`

NewRowsDataSource instantiates a new RowsDataSource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRowsDataSourceWithDefaults

`func NewRowsDataSourceWithDefaults() *RowsDataSource`

NewRowsDataSourceWithDefaults instantiates a new RowsDataSource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *RowsDataSource) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RowsDataSource) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RowsDataSource) SetType(v string)`

SetType sets Type field to given value.


### GetRows

`func (o *RowsDataSource) GetRows() []map[string]AppendRowsRequestRowsInnerValue`

GetRows returns the Rows field if non-nil, zero value otherwise.

### GetRowsOk

`func (o *RowsDataSource) GetRowsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetRowsOk returns a tuple with the Rows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRows

`func (o *RowsDataSource) SetRows(v []map[string]AppendRowsRequestRowsInnerValue)`

SetRows sets Rows field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


