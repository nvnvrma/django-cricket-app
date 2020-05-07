import { Component } from '@angular/core';
import { TeamService } from './services/team.service';

declare var $: any;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app-ui';
  teamDetails: any[];
  playerDetails: any[];
  selectedTeam: string;
  fixtureCount: any;
  fixtureDetails: any[];
  constructor(private teamService: TeamService) {
    this.getAllTeamDetails();
  }

  getAllTeamDetails() {
    this.teamService.fetchAllTeam().subscribe(
      (response) => {
        this.teamDetails = response["data"];
      }
    )
  }

  openModal(team) {
    this.selectedTeam = team.teamName;
    this.teamService.getTeamData(team.teamName).subscribe(
      (response) => {
        this.playerDetails = response["data"];
        $("#teamdetails").modal('show')
      }
    )
  }

  openFixtureModal() {
    console.log(this.fixtureCount)
    $("#fixtureModal").modal('show')
  }

  generateFixtures() {
    this.teamService.generateMatchFixture(this.fixtureCount).subscribe(
      (response) => {
        this.fixtureDetails = response["data"]
      }
    )
  }
}
