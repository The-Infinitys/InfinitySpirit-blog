// The Infinity's Infinity Style Static Site Generator
/*
home/runner/work/InfinitySpirit/InfinitySpirit/The-Infinitys-InfinitySpirit/Program.cs(69,9): error CS8801: Cannot use local variable or local function 'isDirectDrive' declared in a top-level statement in this context. [/home/runner/work/InfinitySpirit/InfinitySpirit/The-Infinitys-InfinitySpirit/The-Infinitys-InfinitySpirit.csproj]

The build failed. Fix the build errors and run again.
*/
using System;
using System.IO;
using System.Text.Json;

Console.WriteLine("-------Infinity Style Static Site Generator-------");
List<string> folderList = GetFolderNames(Environment.CurrentDirectory);
bool isDirectDrive;
isDirectDrive = folderList.Contains("The-Infinitys-InfinitySpirit");
if (isDirectDrive)
{
    Console.WriteLine("Found The-Infinitys-InfinitySpirit. It is release mode");
}
else
{
    Console.WriteLine("Not Found The-Infinitys-InfinitySpiirt. It is test mode");
}

List<string> GetFolderNames(string currentDirectory)
{
    List<string> folderNames = new List<string>();

    foreach (var directory in Directory.EnumerateDirectories(currentDirectory))
    {
        folderNames.Add(Path.GetFileName(directory));
    }

    return folderNames;
}

InfinityStyle.ReadSettingData();

public struct htmlTemp
{
  private htmlTemp(string head, string foot)
  {
    head = "";
    foot = "";
  }
}

public class SettingData
{
  public Dictionary<string, CustomDate>? customDate { get; set; }

  public string? RepositoryName { get; set; }

  public int? RepositoryYear { get; set; }
}

public class CustomDate
{
  public bool? isAutoSet { get; set; }
  public int? CustomYear { get; set; }
  public int? CustomMonth { get; set; }
}

public static class InfinityStyle
{
    public static SettingData? settingData;
  public static void ReadSettingData()
  {
    // 続きはここを見てやろう。
    // https://learn.microsoft.com/ja-jp/dotnet/standard/serialization/system-text-json/deserialization
    StreamReader settingJsonFile;
    if (isDirectDrive){
        settingJsonFile= new StreamReader("./setting/setting.json");
    } else {
        settingJsonFile= new StreamReader("./The-Infinitys-InfinitySpirit/setting/setting.json");
    }
    string settingJsonText = settingJsonFile.ReadToEnd();
    Console.WriteLine("Read setting.json:\n\"\"\"\n" + settingJsonText + "\n\"\"\"");
    settingData = JsonSerializer.Deserialize<SettingData>(
        settingJsonText
    );
    Console.WriteLine("--------------------");
    Console.WriteLine("Read Setting Data");
    Console.WriteLine("--------------------");
    Console.WriteLine("Repository Name: "+settingData?.RepositoryName);
    Console.WriteLine("Repository Year: "+settingData?.RepositoryYear);
    Console.WriteLine("--------------------");
  }
}
