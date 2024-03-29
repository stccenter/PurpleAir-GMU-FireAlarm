## PurpleAir GMU InSitu API Endpoints for FireAlarm

### Below are the details of the InSitu API endpoints to get sensor and reading data.
<table>
  <tr>
    <th>Provider</th>
    <th>Endpoint</th>
    <th>Required Variables</th>
    <th>Optional Variables</th>
    <th>Default Values</th>
    <th>Constraints</th>
  </tr>
<!--   <p>PurpleAir Raw</p> -->
  <tr>
    <td rowspan="4">PurpleAir-GMU-Raw</td>
    <td>sensor_data</td>
    <td>date, min_lon, max_lon, min_lat, max_lat, provider</td>
    <td>variable (can be pm2_5, temperature, or humidity)</td>
    <td>
      <ul>
        <li>variable: pm2_5</li>
      </ul>
    </td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0&provider=PurpleAir-GMU-Raw" target="_blank">https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0&provider=PurpleAir-GMU-Raw</a></td>
  </tr>
  <tr>
    <td>activities</td>
    <td>sensor_ids, sd (start date), provider</td>
    <td></td>
    <td></td>
    <td>
      <ul>
        <li>Maximum of 10 sensors allowed per request.</li>
        <li>End date is not allowed.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="http://insitu-api.stcenter.net/activities?sd=2022-07-01&sensor_ids=34653,9678,90465,14859,56109,142608,14973,55503,73135,39885&provider=PurpleAir-GMU-Raw" target="_blank">https://insitu-api.stcenter.net/activities?sd=2022-07-01&sensor_ids=34653,9678,90465,14859,56109,142608,14973,55503,73135,39885&provider=PurpleAir-GMU-Raw</a></td>
  </tr>
  <!--   <p>PurpleAir Raw Hourly</p> -->
    <tr>
    <td rowspan="4">PurpleAir-GMU-Raw-Hourly</td>
    <td>sensor_data</td>
    <td>date, min_lon, max_lon, min_lat, max_lat, provider</td>
    <td>variable (can be pm2_5, temperature, or humidity)</td>
    <td>      
      <ul>
        <li>variable: pm2_5</li>
      </ul>
    </td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0&provider=PurpleAir-GMU-Raw-Hourly" target="_blank">https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0&provider=PurpleAir-GMU-Raw-Hourly</a></td>
  </tr>
  <tr>
    <td>activities</td>
    <td>sensor_ids, sd (start date), ed (end date), provider</td>
    <td></td>
    <td></td>
    <td>
      <ul>
          <li>Maximum of 500 sensors allowed per request.</li>
          <li>An end date is mandatory for each request.</li>
          <li>The time span between the start date and end date must not exceed 7 days.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="http://insitu-api.stcenter.net/activities?sd=2022-07-01&ed=2022-07-03&sensor_ids=34653,9678,90465,14859,56109,142608,14973,55503,73135,39885&provider=PurpleAir-GMU-Raw-Hourly" target="_blank">https://insitu-api.stcenter.net/activities?sd=2022-07-01&ed=2022-07-03&sensor_ids=34653,9678,90465,14859,56109,142608,14973,55503,73135,39885&provider=PurpleAir-GMU-Raw-Hourly</a></td>
  </tr>
   <!--   <p>PurpleAir Intermediate</p> -->
    <tr>
    <td rowspan="4">PurpleAir-GMU-Intermediate</td>
    <td>sensor_data</td>
    <td>date, min_lon, max_lon, min_lat, max_lat, provider</td>
    <td>variable (can be pm2_5, temperature, or humidity)</td>
    <td>      
      <ul>
        <li>variable: pm2_5</li>
      </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-118.67&max_lon=-118.15&min_lat=33.70&max_lat=34.34&provider=PurpleAir-GMU-Intermediate" target="_blank">https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-118.67&max_lon=-118.15&min_lat=33.70&max_lat=34.34&provider=PurpleAir-GMU-Intermediate</a></td>
  </tr>
  <tr>
    <td>activities</td>
    <td>sensor_ids, sd (start date), ed (end date), provider</td>
    <td></td>
    <td></td>
    <td>
      <ul>
          <li>Maximum of 500 sensors allowed per request.</li>
          <li>An end date is mandatory for each request.</li>
          <li>The time span between the start date and end date must not exceed 7 days.</li>
          <li>Start and end dates cannot be the same.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="http://insitu-api.stcenter.net/activities?sd=2022-07-01&ed=2022-07-03&sensor_ids=96771,4069,130445,96855,96243,27235,34873,130445,90323,80807,23945,56899&provider=PurpleAir-GMU-Intermediate" target="_blank">https://insitu-api.stcenter.net/activities?sd=2022-07-01&ed=2022-07-03&sensor_ids=96771,4069,130445,96855,96243,27235,34873,130445,90323,80807,23945,56899&provider=PurpleAir-GMU-Intermediate</a></td>
  </tr>
    <!--   <p>PurpleAir Calibrate</p> -->
    <tr>
    <td rowspan="4">PurpleAir-GMU-Cal</td>
    <td>sensor_data</td>
    <td>date, min_lon, max_lon, min_lat, max_lat, provider</td>
    <td>variable (can be pm2_5, temperature, or humidity)</td>
    <td>      
      <ul>
        <li>variable: pm2_5</li>
      </ul>
    </td>
    <td>Bounding box must be within Los Angeles: [33.70, -118.67] to [34.34, -118.15]</td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-118.67&max_lon=-118.15&min_lat=33.70&max_lat=34.34&provider=PurpleAir-GMU-Cal" target="_blank">https://insitu-api.stcenter.net/sensor_data?date=2022-07-01&variable=pm2_5&min_lon=-118.67&max_lon=-118.15&min_lat=33.70&max_lat=34.34&provider=PurpleAir-GMU-Cal</a></td>
  </tr>
  <tr>
    <td>activities</td>
    <td>sensor_ids, sd (start date), ed (end date), provider</td>
    <td></td>
    <td></td>
    <td>
      <ul>
          <li>Maximum of 500 sensors allowed per request.</li>
          <li>An end date is mandatory for each request.</li>
          <li>The time span between the start date and end date must not exceed 7 days.</li>
          <li>Start and end dates cannot be the same.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/activities?sd=2022-07-01&ed=2022-07-02&sensor_ids=96771,4069,130445,96855,96243,27235,34873,130445,90323,80807,23945,56899&provider=PurpleAir-GMU-Cal" target="_blank">https://insitu-api.stcenter.net/activities?sd=2022-07-01&ed=2022-07-02&sensor_ids=96771,4069,130445,96855,96243,27235,34873,130445,90323,80807,23945,56899&provider=PurpleAir-GMU-Cal</a></td>
  </tr>
</table>

### Below are the details of the InSitu API endpoints to get statistics of each sensor.

<table>
  <tr>
    <th>Provider</th>
    <th>Endpoint</th>
    <th>Required Variables</th>
    <th>Optional Variables</th>
    <th>Default Values</th>
    <th>Constraints</th>
  </tr>
<!--   <p>PurpleAir Raw</p> -->
  <tr>
    <td rowspan="2">PurpleAir-GMU-Raw</td>
    <td>statistics</td>
    <td>provider, project, startTime, endTime</td>
    <td></td>
    <td>
    </td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Raw&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z" target="_blank">https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Raw&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z</a></td>
  </tr>
<!--   <p>PurpleAir Raw Hourly</p> -->
   <tr>
    <td rowspan="2">PurpleAir-GMU-Raw-Hourly</td>
    <td>statistics</td>
    <td>provider, project, startTime, endTime</td>
    <td></td>
    <td>
    </td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Raw-Hourly&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z" target="_blank">https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Raw-Hourly&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z</a></td>
  </tr>
  <!--   <p>PurpleAir Intermediate</p> -->
   <tr>
    <td rowspan="2">PurpleAir-GMU-Intermediate</td>
    <td>statistics</td>
    <td>provider, project, startTime, endTime</td>
    <td></td>
    <td>
    </td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Intermediate&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z" target="_blank">https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Intermediate&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z</a></td>
  </tr>

    <!--   <p>PurpleAir Cal</p> -->
   <tr>
    <td rowspan="2">PurpleAir-GMU-Cal</td>
    <td>statistics</td>
    <td>provider, project, startTime, endTime</td>
    <td></td>
    <td>
    </td>
    <td>No specific constraints</td>
  </tr>
  <tr>
    <td colspan="5"><strong>Sample Request:</strong> <a href="https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Cal&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z" target="_blank">https://insitu-api.stcenter.net/statistics?provider=PurpleAir-GMU-Cal&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z</a></td>
  </tr>
</table>
