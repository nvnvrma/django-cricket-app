import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class TeamService {

  url = "http://127.0.0.1:8000/teams/all/"
  url_fixture = "http://127.0.0.1:8000/match/fixtures/"

  constructor(private http : HttpClient) {

   }

   fetchAllTeam() {
     return this.http.get(this.url)
   }

   getTeamData(name : any) {
     let data = {"teamName" : name}
    return this.http.post(this.url,data)
   }

   generateMatchFixture(count) {
     let data = {"fixturesCount" : count}
     return this.http.post(this.url_fixture,data)
   }


}
