## PurpleAir GMU InSitu API Endpoints for FireAlarm

Below are the details of the available InSitu API endpoints:
<table>
  <tr>
    <th>Provider</th>
    <th>Endpoint</th>
    <th>Required Variables</th>
    <th>Optional Variables</th>
    <th>Constraints</th>
  </tr>
  <tr>
    <td rowspan="4">PurpleAir-GMU-Raw</td>
    <td>/sensor_data</td>
    <td>date, min_lon, max_lon, min_lat, max_lat</td>
    <td>variable, provider</td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="4"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0">https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0</a></td>
  </tr>
  <tr>
    <td>/activities</td>
    <td>sensor_ids, sd (start date)</td>
    <td>ed (end date), provider</td>
    <td>Max 10 sensors, no end date for raw data</td>
  </tr>
  <tr>
    <td colspan="4"><strong>Sample Request:</strong> <a href="http://insitu-api.stcenter.net/activities?sensor_ids=ID1,ID2,...&sd=YYYY-MM-DD">http://insitu-api.stcenter.net/activities?sensor_ids=ID1,ID2,...&sd=YYYY-MM-DD</a></td>
  </tr>
</table>




