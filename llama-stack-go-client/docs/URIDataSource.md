# URIDataSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "uri"]
**Uri** | **string** | The dataset can be obtained from a URI. E.g. - \&quot;https://mywebsite.com/mydata.jsonl\&quot; - \&quot;lsfs://mydata.jsonl\&quot; - \&quot;data:csv;base64,{base64_content}\&quot; | 

## Methods

### NewURIDataSource

`func NewURIDataSource(type_ string, uri string, ) *URIDataSource`

NewURIDataSource instantiates a new URIDataSource object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewURIDataSourceWithDefaults

`func NewURIDataSourceWithDefaults() *URIDataSource`

NewURIDataSourceWithDefaults instantiates a new URIDataSource object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *URIDataSource) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *URIDataSource) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *URIDataSource) SetType(v string)`

SetType sets Type field to given value.


### GetUri

`func (o *URIDataSource) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *URIDataSource) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *URIDataSource) SetUri(v string)`

SetUri sets Uri field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


