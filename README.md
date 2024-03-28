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
    <td>variable (can be pm2_5, temperature, or humidity), provider</td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="4"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0" target="_blank">https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0</a></td>
  </tr>
  <tr>
    <td>/activities</td>
    <td>sensor_ids, sd (start date)</td>
    <td>provider</td>
    <td>Max 10 sensors allowed; End date is not allowed</td>
  </tr>
  <tr>
    <td colspan="4"><strong>Sample Request:</strong> <a href="http://insitu-api.stcenter.net/activities?sd=2022-07-01&sensor_ids=34653,9678,90465,14859,56109,142608,14973,55503,73135,39885&provider=PurpleAir-GMU-Raw" target="_blank">https://insitu-api.stcenter.net/activities?sd=2022-07-01&sensor_ids=34653,9678,90465,14859,56109,142608,14973,55503,73135,39885&provider=PurpleAir-GMU-Raw</a></td>
  </tr>
</table>




